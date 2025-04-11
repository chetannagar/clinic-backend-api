from django.shortcuts import render
from rest_framework import viewsets
from doctors.models import Doctor, DoctorAvailability
from doctors.serializers import DoctorSerializer, DoctorAvailabilitySerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer