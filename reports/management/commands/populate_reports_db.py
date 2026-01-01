# myapp/management/commands/populate_reports_db.py
import itertools
import random

from django.core.management.base import BaseCommand

from appointments.models import Appointment
from appointments.factories import AppointmentFactory
from reports.factories import MedicalReportFactory, PrescriptionFactory

DEFAULT_MEDICAL_REPORT_COUNT = 10
DEFAULT_PRESCRIPTION_COUNT = 10

class Command(BaseCommand):
    """Django management command to populate the database with dummy medical reports and prescriptions data."""
    help = "Populates the database with dummy medical reports and prescriptions data."

    def handle(self, *args, **options):
        appointments = list(Appointment.objects.all())
        if not appointments:
            appointments = list(AppointmentFactory.create_batch(DEFAULT_MEDICAL_REPORT_COUNT))

        medical_reports = []
        for appointment in appointments[:DEFAULT_MEDICAL_REPORT_COUNT]:
            medical_reports.append(
                MedicalReportFactory(
                    appointment=appointment,
                    patient=appointment.patient,
                    doctor=appointment.doctor,
                )
            )

        prescriptions = []
        for appointment in itertools.islice(iter(appointments), DEFAULT_PRESCRIPTION_COUNT):
            prescriptions.append(
                PrescriptionFactory(
                    appointment=appointment,
                    patient=appointment.patient,
                    doctor=appointment.doctor,
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully populated {len(medical_reports)} medical reports and {len(prescriptions)} prescriptions"
            )
        )