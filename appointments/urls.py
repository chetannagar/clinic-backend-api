from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appointments.views import (
    AppointmentViewSet,
    AppointmentBookView,
    AppointmentListView,
    AppointmentDetailView,
    AppointmentUpdateView,
    AppointmentStatusView,
    AppointmentCancelView,
)

router = DefaultRouter()
router.register(r'', AppointmentViewSet)

urlpatterns = [
    path("book/", AppointmentBookView.as_view(), name="appointment-book"),
    path("list/", AppointmentListView.as_view(), name="appointment-list"),
    path("<uuid:pk>/", AppointmentDetailView.as_view(), name="appointment-detail"),
    path("<uuid:pk>/update/", AppointmentUpdateView.as_view(), name="appointment-update"),
    path("<uuid:pk>/status/", AppointmentStatusView.as_view(), name="appointment-status"),
    path("<uuid:pk>/cancel/", AppointmentCancelView.as_view(), name="appointment-cancel"),
]
urlpatterns += router.urls
