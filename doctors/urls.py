from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doctors.views import DoctorViewSet, DoctorAvailabilityViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'doctor-availabilities', DoctorAvailabilityViewSet)

urlpatterns = router.urls
