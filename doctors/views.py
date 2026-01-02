from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from doctors.models import Doctor, DoctorAvailability
from doctors.serializers import DoctorSerializer, DoctorAvailabilitySerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer


class DoctorListView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class DoctorDetailView(RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class DoctorApproveView(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.is_approved = True
        doctor.approved_at = timezone.now()
        doctor.approval_notes = request.data.get("approval_notes", "")
        doctor.save(update_fields=["is_approved", "approved_at", "approval_notes"])
        return Response(DoctorSerializer(doctor).data, status=status.HTTP_200_OK)


class DoctorAvailabilityByDoctorView(ListAPIView):
    serializer_class = DoctorAvailabilitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DoctorAvailability.objects.filter(doctor_id=self.kwargs["pk"])
