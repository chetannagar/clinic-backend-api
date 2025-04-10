from django.contrib import admin
from clinic_settings.models import ClinicSetting, Review, AuditLog, AdminActionLog

admin.site.register(ClinicSetting)
admin.site.register(Review)
admin.site.register(AuditLog)
admin.site.register(AdminActionLog)