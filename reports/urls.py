from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reports.views import MedicalReportViewSet, PrescriptionViewSet

router = DefaultRouter()
router.register(r'medical-reports', MedicalReportViewSet)
router.register(r'prescriptions', PrescriptionViewSet)

urlpatterns = router.urls
