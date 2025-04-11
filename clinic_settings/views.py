from django.shortcuts import render
from rest_framework import viewsets
from clinic_settings.models import ClinicSetting, Review, AuditLog, AdminActionLog
from clinic_settings.serializers import ClinicSettingSerializer, ReviewSerializer, AuditLogSerializer, AdminActionLogSerializer

class ClinicSettingViewSet(viewsets.ModelViewSet):
    queryset = ClinicSetting.objects.all()
    serializer_class = ClinicSettingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer

class AdminActionLogViewSet(viewsets.ModelViewSet):
    queryset = AdminActionLog.objects.all()
    serializer_class = AdminActionLogSerializer