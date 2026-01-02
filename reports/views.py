from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from reports.models import MedicalReport, Prescription
from reports.serializers import MedicalReportSerializer, PrescriptionSerializer

class MedicalReportViewSet(viewsets.ModelViewSet):
    queryset = MedicalReport.objects.all()
    serializer_class = MedicalReportSerializer

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class MedicalReportUploadView(CreateAPIView):
    queryset = MedicalReport.objects.all()
    serializer_class = MedicalReportSerializer
    permission_classes = [IsAuthenticated]


class MedicalReportDetailView(RetrieveAPIView):
    queryset = MedicalReport.objects.all()
    serializer_class = MedicalReportSerializer
    permission_classes = [IsAuthenticated]


class MedicalReportPatientListView(ListAPIView):
    serializer_class = MedicalReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MedicalReport.objects.filter(patient_id=self.kwargs["patient_id"])


class MedicalReportDeleteView(DestroyAPIView):
    queryset = MedicalReport.objects.all()
    serializer_class = MedicalReportSerializer
    permission_classes = [IsAuthenticated]


class PrescriptionCreateView(CreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]


class PrescriptionDetailView(RetrieveAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]


class PrescriptionPatientListView(ListAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Prescription.objects.filter(patient_id=self.kwargs["patient_id"])


class PrescriptionUpdateView(UpdateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]


class PrescriptionDeleteView(DestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]
