from django.urls import path
from clinic_settings.views import AuditLogListView, AuditLogDetailView

urlpatterns = [
    path("list/", AuditLogListView.as_view(), name="audit-log-list"),
    path("<uuid:pk>/", AuditLogDetailView.as_view(), name="audit-log-detail"),
]
