from django.contrib import admin
from clinic_settings.models import Availability, ClinicSetting, Review, AuditLog

admin.site.register(Availability)
admin.site.register(ClinicSetting)
admin.site.register(Review)
admin.site.register(AuditLog)