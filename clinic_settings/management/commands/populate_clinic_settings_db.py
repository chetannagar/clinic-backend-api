# myapp/management/commands/populate_clinic_settings_db.py
import random

from django.core.management.base import BaseCommand
from clinic_settings.factories import (
    AdminActionLogFactory,
    AuditLogFactory,
    ClinicSettingFactory,
    ReviewFactory,
)

from doctors.models import Doctor
from patients.models import Patient
from users.factories import UserFactory
from users.models import User

DEFAULT_CLINIC_SETTINGS_COUNT = 3
DEFAULT_REVIEW_COUNT = 15
DEFAULT_AUDIT_LOG_COUNT = 20
DEFAULT_ADMIN_ACTION_LOG_COUNT = 10


class Command(BaseCommand):
    """Django management command to populate the database with dummy clinic settings data."""
    help = "Populates the database with dummy clinic settings data."

    def handle(self, *args, **options):
        clinic_settings = ClinicSettingFactory.create_batch(DEFAULT_CLINIC_SETTINGS_COUNT)

        patients = list(Patient.objects.all())
        if not patients:
            from patients.factories import PatientFactory

            patients = list(PatientFactory.create_batch(DEFAULT_REVIEW_COUNT))

        doctors = list(Doctor.objects.all())
        if not doctors:
            from doctors.factories import DoctorFactory

            doctors = list(DoctorFactory.create_batch(max(5, DEFAULT_REVIEW_COUNT // 3)))

        reviews = []
        for _ in range(DEFAULT_REVIEW_COUNT):
            reviews.append(ReviewFactory(patient=random.choice(patients), doctor=random.choice(doctors)))

        users = list(User.objects.all())
        if not users:
            users = list(UserFactory.create_batch(10))

        audit_logs = [AuditLogFactory(user=random.choice(users)) for _ in range(DEFAULT_AUDIT_LOG_COUNT)]

        admins = [u for u in users if u.role == User.ROLE_ADMIN]
        if not admins:
            admins = [UserFactory(role=User.ROLE_ADMIN)]

        admin_action_logs = [
            AdminActionLogFactory(user=random.choice(admins)) for _ in range(DEFAULT_ADMIN_ACTION_LOG_COUNT)
        ]

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully populated {len(clinic_settings)} clinic settings, "
                f"{len(reviews)} reviews, {len(audit_logs)} audit logs, and "
                f"{len(admin_action_logs)} admin action logs"
            )
        )
