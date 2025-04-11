from rest_framework import serializers
from clinic_settings.models import ClinicSetting, Review, AuditLog, AdminActionLog

class ClinicSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicSetting
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'

class AdminActionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminActionLog
        fields = '__all__'
