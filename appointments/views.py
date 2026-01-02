from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentBookView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]


class AppointmentListView(ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.filter(
            Q(patient__user=user) | Q(doctor__user=user)
        ).distinct()


class AppointmentDetailView(RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]


class AppointmentUpdateView(UpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]


class AppointmentStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        status_value = request.data.get("status")
        if not status_value:
            return Response({"detail": "status is required."}, status=status.HTTP_400_BAD_REQUEST)
        appointment.status = status_value
        appointment.save(update_fields=["status"])
        return Response(AppointmentSerializer(appointment).data, status=status.HTTP_200_OK)


class AppointmentCancelView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        appointment.status = Appointment.STATUS_CANCELED
        appointment.save(update_fields=["status"])
        return Response(AppointmentSerializer(appointment).data, status=status.HTTP_200_OK)
