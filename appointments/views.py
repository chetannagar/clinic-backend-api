from django.shortcuts import render
from rest_framework import viewsets
from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer