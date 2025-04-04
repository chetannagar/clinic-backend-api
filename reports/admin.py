from django.contrib import admin
from reports.models import MedicalReport, Prescription

admin.site.register(MedicalReport)
admin.site.register(Prescription)