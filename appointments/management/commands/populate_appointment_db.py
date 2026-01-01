# myapp/management/commands/populate_appointment_db.py
import random
from django.core.management.base import BaseCommand
from appointments.factories import AppointmentFactory

from doctors.factories import DoctorFactory
from doctors.models import Doctor
from patients.factories import PatientFactory
from patients.models import Patient

DEFAULT_APPOINTMENT_COUNT = 20


class Command(BaseCommand):
    """Django management command to populate the database with dummy appointment data."""
    help = "Populates the database with dummy appointment data"

    def handle(self, *args, **options):
        patients = list(Patient.objects.all())
        if not patients:
            patients = list(PatientFactory.create_batch(DEFAULT_APPOINTMENT_COUNT))

        doctors = list(Doctor.objects.all())
        if not doctors:
            doctors = list(DoctorFactory.create_batch(max(5, DEFAULT_APPOINTMENT_COUNT // 4)))

        appointments = []
        for _ in range(DEFAULT_APPOINTMENT_COUNT):
            patient = random.choice(patients)
            doctor = random.choice(doctors)
            appointments.append(AppointmentFactory(patient=patient, doctor=doctor))

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully populated database with {len(appointments)} dummy appointments"
            )
        )
