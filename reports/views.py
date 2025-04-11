from django.shortcuts import render
from rest_framework import viewsets
from reports.models import MedicalReport, Prescription
from reports.serializers import MedicalReportSerializer, PrescriptionSerializer

class MedicalReportViewSet(viewsets.ModelViewSet):
    queryset = MedicalReport.objects.all()
    serializer_class = MedicalReportSerializer

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer