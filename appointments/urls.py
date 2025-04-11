from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appointments.views import AppointmentViewSet

router = DefaultRouter()
router.register(r'', AppointmentViewSet)

urlpatterns = router.urls
