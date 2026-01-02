from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reports.views import (
    MedicalReportViewSet,
    PrescriptionViewSet,
    MedicalReportUploadView,
    MedicalReportDetailView,
    MedicalReportPatientListView,
    MedicalReportDeleteView,
    PrescriptionCreateView,
    PrescriptionDetailView,
    PrescriptionPatientListView,
    PrescriptionUpdateView,
    PrescriptionDeleteView,
)

router = DefaultRouter()
router.register(r'medical-reports', MedicalReportViewSet)
router.register(r'prescriptions', PrescriptionViewSet)

urlpatterns = [
    path("upload/", MedicalReportUploadView.as_view(), name="report-upload"),
    path("<uuid:pk>/", MedicalReportDetailView.as_view(), name="report-detail"),
    path("patient/<uuid:patient_id>/", MedicalReportPatientListView.as_view(), name="report-patient-list"),
    path("<uuid:pk>/delete/", MedicalReportDeleteView.as_view(), name="report-delete"),
    path("prescriptions/create/", PrescriptionCreateView.as_view(), name="prescription-create"),
    path("prescriptions/<uuid:pk>/", PrescriptionDetailView.as_view(), name="prescription-detail"),
    path("prescriptions/patient/<uuid:patient_id>/", PrescriptionPatientListView.as_view(), name="prescription-patient-list"),
    path("prescriptions/<uuid:pk>/update/", PrescriptionUpdateView.as_view(), name="prescription-update"),
    path("prescriptions/<uuid:pk>/delete/", PrescriptionDeleteView.as_view(), name="prescription-delete"),
]
urlpatterns += router.urls
