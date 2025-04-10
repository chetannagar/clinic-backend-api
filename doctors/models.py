import uuid
from django.db import models

from users.models import User

class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)
    qualifications = models.TextField(blank=True)
    experience = models.PositiveIntegerField()
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

class DoctorAvailability(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availabilities')
    DAY_MONDAY = 'Monday'
    DAY_TUESDAY = 'Tuesday'
    DAY_WEDNESDAY = 'Wednesday'
    DAY_THURSDAY = 'Thursday'
    DAY_FRIDAY = 'Friday'
    DAY_SATURDAY = 'Saturday'
    DAY_SUNDAY = 'Sunday'
    DAYS_OF_WEEK = [
        (DAY_MONDAY, 'Monday'),
        (DAY_TUESDAY, 'Tuesday'),
        (DAY_WEDNESDAY, 'Wednesday'),
        (DAY_THURSDAY, 'Thursday'),
        (DAY_FRIDAY, 'Friday'),
        (DAY_SATURDAY, 'Saturday'),
        (DAY_SUNDAY, 'Sunday'),
    ]
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Doctor Availability"
        verbose_name_plural = "Doctor Availabilities"
        ordering = ['doctor', 'day_of_week', 'start_time']

    def __str__(self):
        return f"{self.doctor.user.get_full_name()} - {self.day_of_week} ({self.start_time} to {self.end_time})"