from django.contrib import admin
from doctors.models import Doctor, DoctorAvailability

admin.site.register(Doctor)  # Register the Doctor model
admin.site.register(DoctorAvailability)  # Register the DoctorAvailability model