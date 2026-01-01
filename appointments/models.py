import uuid
from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    STATUS_SCHEDULED = 'Scheduled'
    STATUS_COMPLETED = 'Completed'
    STATUS_CANCELED = 'Canceled'
    STATUS_RESCHEDULED = 'Rescheduled'
    STATUS_NO_SHOW = 'No-show'
    STATUS_CHOICES = [
        (STATUS_SCHEDULED, 'Scheduled'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELED, 'Canceled'),
        (STATUS_RESCHEDULED, 'Rescheduled'),
        (STATUS_NO_SHOW, 'No-show'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_SCHEDULED)
    reason = models.TextField(blank=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.user.email} - {self.doctor.user.email} - {self.appointment_date}"

    class Meta:
        ordering = ['appointment_date', 'appointment_time']
        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'appointment_date', 'appointment_time'],
                name='unique_doctor_appointment_slot'
            ),
            models.UniqueConstraint(
                fields=['patient', 'appointment_date', 'appointment_time'],
                name='unique_patient_appointment_slot'
            ),
            models.CheckConstraint(
                check=models.Q(appointment_time__isnull=False),
                name='appointment_time_not_null'
            ),
        ]