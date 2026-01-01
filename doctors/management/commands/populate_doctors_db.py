# myapp/management/commands/populate_doctors_db.py
from django.core.management.base import BaseCommand

from doctors.factories import DoctorAvailabilityFactory, DoctorFactory

DEFAULT_DOCTOR_COUNT = 10
AVAILABILITIES_PER_DOCTOR = 2

class Command(BaseCommand):
    """Django management command to populate the database with dummy doctors and their availability data."""
    help = "Populates the database with dummy doctors and availability"

    def handle(self, *args, **options):
        doctors = DoctorFactory.create_batch(DEFAULT_DOCTOR_COUNT)

        for doctor in doctors:
            DoctorAvailabilityFactory.create_batch(AVAILABILITIES_PER_DOCTOR, doctor=doctor)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully populated database with {len(doctors)} dummy doctors and availability slots"
            )
        )