# myapp/management/commands/populate_db_master.py
import random

from django.core.management.base import BaseCommand

from appointments.factories import AppointmentFactory
from clinic_settings.factories import (
    AdminActionLogFactory,
    AuditLogFactory,
    ClinicSettingFactory,
    ReviewFactory,
)
from doctors.factories import DoctorAvailabilityFactory, DoctorFactory
from notifications.factories import MessageFactory, NotificationFactory
from patients.factories import PatientFactory
from payments.factories import InvoiceFactory, PaymentFactory
from reports.factories import MedicalReportFactory, PrescriptionFactory
from users.factories import UserFactory
from users.models import User

# Constants for batch sizes
DOCTORS_BATCH_SIZE = 5
PATIENTS_BATCH_SIZE = 10
ADMIN_BATCH_SIZE = 10
STAFF_BATCH_SIZE = 75
NUM_APPOINTMENTS = 20
NUM_AVAILABILITIES = 2
NUM_CLINIC_SETTINGS = 3
NUM_REVIEWS = 15
NUM_AUDIT_LOGS = 20
NUM_ADMIN_ACTIONS = 20
NUM_NOTIFICATIONS = 30
NUM_MESSAGES = 20
NUM_PAYMENTS = 10
NUM_INVOICES = 10
NUM_PRESCRIPTIONS = 10

class Command(BaseCommand):
    """Command to populate the database with dummy data."""
    help = "Populates the database with dummy data"

    def handle(self, *args, **options):
        # Create users by role
        doctor_users = UserFactory.create_batch(DOCTORS_BATCH_SIZE, role=User.ROLE_DOCTOR)
        patient_users = UserFactory.create_batch(PATIENTS_BATCH_SIZE, role=User.ROLE_PATIENT)
        admin_users = UserFactory.create_batch(ADMIN_BATCH_SIZE, role=User.ROLE_ADMIN)
        staff_users = UserFactory.create_batch(STAFF_BATCH_SIZE, role=User.ROLE_STAFF)
        users = doctor_users + patient_users + admin_users + staff_users

        # Create patients and doctors using specific users
        patients = [PatientFactory(user=user) for user in patient_users]
        doctors = [DoctorFactory(user=user) for user in doctor_users]

        # Appointments
        appointments = [
            AppointmentFactory(
                patient=random.choice(patients),
                doctor=random.choice(doctors)
            )
            for _ in range(NUM_APPOINTMENTS)
        ]

        # Doctor availability
        for _ in range(NUM_AVAILABILITIES):
            DoctorAvailabilityFactory(doctor=random.choice(doctors))

        # Clinic settings
        clinic_settings = ClinicSettingFactory.create_batch(NUM_CLINIC_SETTINGS)

        # Reviews - ensure unique patient-doctor pairs
        used_review_pairs = set()
        while len(used_review_pairs) < NUM_REVIEWS:
            patient = random.choice(patients)
            doctor = random.choice(doctors)
            key = (patient.id, doctor.id)
            if key in used_review_pairs:
                continue
            used_review_pairs.add(key)
            ReviewFactory(patient=patient, doctor=doctor)

        # Audit logs
        audit_logs = [AuditLogFactory(user=random.choice(users)) for _ in range(NUM_AUDIT_LOGS)]

        # Admin action logs
        for _ in range(NUM_ADMIN_ACTIONS):
            user = random.choice(users)
            AdminActionLogFactory(user=user)

        # Notifications
        for _ in range(NUM_NOTIFICATIONS):
            user = random.choice(users)
            appointment = random.choice(appointments) if appointments else None
            NotificationFactory(user=user, appointment=appointment)

        # Messages
        for _ in range(NUM_MESSAGES):
            sender = random.choice(users)
            receiver = random.choice(users)
            MessageFactory(sender=sender, receiver=receiver)

        # Payments
        for _ in range(NUM_PAYMENTS):
            appointment = random.choice(appointments)
            PaymentFactory(appointment=appointment)

        # Invoices
        for _ in range(NUM_INVOICES):
            appointment = random.choice(appointments)
            InvoiceFactory(appointment=appointment)

        # Medical reports for first 10 appointments
        for appointment in appointments[:10]:
            MedicalReportFactory(
                patient=appointment.patient,
                doctor=appointment.doctor,
                appointment=appointment
            )

        # Prescriptions
        for appointment in appointments[:NUM_PRESCRIPTIONS]:
            PrescriptionFactory(
                appointment=appointment,
                patient=appointment.patient,
                doctor=appointment.doctor,
            )

        # Final confirmation
        self.stdout.write(
            self.style.SUCCESS("Successfully populated database with dummy data")
        )
