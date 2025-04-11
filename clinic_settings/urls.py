from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clinic_settings.views import ClinicSettingViewSet, ReviewViewSet, AuditLogViewSet, AdminActionLogViewSet

router = DefaultRouter()
router.register(r'clinic-settings', ClinicSettingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'audit-logs', AuditLogViewSet)
router.register(r'admin-action-logs', AdminActionLogViewSet)

urlpatterns = router.urls
