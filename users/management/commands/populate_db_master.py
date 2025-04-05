# myapp/management/commands/populate_db_master.py
from django.core.management.base import BaseCommand
from users.factories import UserFactory
from patients.factories import PatientFactory
from doctors.factories import DoctorFactory
from appointments.factories import AppointmentFactory
from clinic_settings.factories import AvailabilityFactory, ClinicSettingFactory, ReviewFactory, AuditLogFactory
from notifications.factories import NotificationFactory, MessageFactory
from payments.factories import PaymentFactory, InvoiceFactory
from reports.factories import MedicalReportFactory, PrescriptionFactory
import random

from users.models import User

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **options):
        # Create users first
        users = UserFactory.create_batch(10)

        # Create patients and doctors using the created users
        patients = [PatientFactory(user=random.choice(users)) for _ in range(5)]
        doctors = [DoctorFactory(user=random.choice(users), role='Doctor') for _ in range(5)] # ensure doctor role

        # Create other objects, reusing patients and doctors
        appointments = AppointmentFactory.create_batch(20, patient=lambda: random.choice(patients), doctor=lambda: random.choice(doctors))
        availability = AvailabilityFactory.create_batch(10, doctor=lambda: random.choice(doctors))
        clinic_settings = ClinicSettingFactory.create_batch(3)
        reviews = ReviewFactory.create_batch(15, patient=lambda: random.choice(patients), doctor=lambda: random.choice(doctors))
        audit_logs = AuditLogFactory.create_batch(20, user=lambda: random.choice(users))
        notifications = NotificationFactory.create_batch(30, user=lambda: random.choice(users), appointment=lambda: random.choice(appointments) if appointments else None)
        messages = MessageFactory.create_batch(20, sender=lambda: random.choice(users), receiver=lambda: random.choice(users))
        payments = PaymentFactory.create_batch(10, patient=lambda: random.choice(patients), doctor=lambda: random.choice(doctors), appointment=lambda: random.choice(appointments))
        invoices = InvoiceFactory.create_batch(10, patient=lambda: random.choice(patients), appointment=lambda: random.choice(appointments))
        medical_reports = MedicalReportFactory.create_batch(10, patient=lambda: random.choice(patients), doctor=lambda: random.choice(doctors), appointment=lambda: random.choice(appointments) if appointments else None)
        prescriptions = PrescriptionFactory.create_batch(10, patient=lambda: random.choice(patients), doctor=lambda: random.choice(doctors))

        self.stdout.write(self.style.SUCCESS('Successfully populated database with dummy data'))