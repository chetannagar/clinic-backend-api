from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doctors.views import (
    DoctorViewSet,
    DoctorAvailabilityViewSet,
    DoctorListView,
    DoctorDetailView,
    DoctorApproveView,
    DoctorAvailabilityByDoctorView,
)

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'doctor-availabilities', DoctorAvailabilityViewSet)

urlpatterns = [
    path("list/", DoctorListView.as_view(), name="doctor-list"),
    path("<uuid:pk>/", DoctorDetailView.as_view(), name="doctor-detail"),
    path("<uuid:pk>/approve/", DoctorApproveView.as_view(), name="doctor-approve"),
    path("<uuid:pk>/availability/", DoctorAvailabilityByDoctorView.as_view(), name="doctor-availability"),
]
urlpatterns += router.urls
