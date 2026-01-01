# myapp/management/commands/populate_patients_db.py
from django.core.management.base import BaseCommand

from patients.factories import PatientFactory

DEFAULT_PATIENT_COUNT = 20

class Command(BaseCommand):
    """Django management command to populate the database with dummy patients data."""
    help = "Populates the database with dummy patients data"

    def handle(self, *args, **options):
        patients = PatientFactory.create_batch(DEFAULT_PATIENT_COUNT)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated database with {len(patients)} dummy patients")
        )