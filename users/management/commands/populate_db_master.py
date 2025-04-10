# myapp/management/commands/populate_db_master.py
from django.core.management.base import BaseCommand
import factory
from users.models import User
from users.factories import UserFactory
from patients.factories import PatientFactory
from doctors.factories import DoctorFactory, DoctorAvailabilityFactory
from appointments.factories import AppointmentFactory
from clinic_settings.factories import ClinicSettingFactory, ReviewFactory, AuditLogFactory, AdminActionLogFactory
from notifications.factories import NotificationFactory, MessageFactory
from payments.factories import PaymentFactory, InvoiceFactory
from reports.factories import MedicalReportFactory, PrescriptionFactory
import random


class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **options):
        # Create users by role
        doctor_users = UserFactory.create_batch(5, role=User.ROLE_DOCTOR)
        patient_users = UserFactory.create_batch(10, role=User.ROLE_PATIENT)
        # remaining users for admin, receptionists, etc.
        other_users = UserFactory.create_batch(85)
        users = doctor_users + patient_users + other_users

        # Create patients and doctors using the appropriate users
        patients = [PatientFactory(user=user) for user in patient_users]
        doctors = [DoctorFactory(user=user) for user in doctor_users]

        # Create other objects, reusing patients and doctors
        appointments = [
            AppointmentFactory(patient=random.choice(
                patients), doctor=random.choice(doctors))
            for _ in range(20)
        ]
        availability = [DoctorAvailabilityFactory.create(
            doctor=random.choice(doctors)) for _ in range(2)]
        clinic_settings = ClinicSettingFactory.create_batch(3)
        reviews = ReviewFactory.create_batch(15,
                                             patient=factory.LazyFunction(
                                                 lambda: random.choice(patients)),
                                             doctor=factory.LazyFunction(
                                                 lambda: random.choice(doctors))
                                             )
        audit_logs = [AuditLogFactory(user=random.choice(users))
                      for _ in range(20)]
        admin_action_logs = AdminActionLogFactory.create_batch(
            20, user=factory.LazyFunction(lambda: random.choice(users)))
        notifications = NotificationFactory.create_batch(30,
                                                         user=factory.LazyFunction(
                                                             lambda: random.choice(users)),
                                                         appointment=factory.LazyFunction(lambda: random.choice(
                                                             appointments) if appointments else None)
                                                         )
        messages = MessageFactory.create_batch(20,
                                               sender=factory.LazyFunction(
                                                   lambda: random.choice(users)),
                                               receiver=factory.LazyFunction(
                                                   lambda: random.choice(users))
                                               )
        payments = PaymentFactory.create_batch(10,
                                               patient=factory.LazyFunction(
                                                   lambda: random.choice(patients)),
                                               doctor=factory.LazyFunction(
                                                   lambda: random.choice(doctors)),
                                               appointment=factory.LazyFunction(
                                                   lambda: random.choice(appointments))
                                               )
        invoices = InvoiceFactory.create_batch(10,
                                               patient=factory.LazyFunction(
                                                   lambda: random.choice(patients)),
                                               appointment=factory.LazyFunction(
                                                   lambda: random.choice(appointments))
                                               )

        # Ensure unique appointments for medical reports
        medical_reports = [
            MedicalReportFactory(
                patient=random.choice(patients),
                doctor=random.choice(doctors),
                appointment=appointment
            )
            # Use only the first 10 appointments
            for appointment in appointments[:10]
        ]

        prescriptions = PrescriptionFactory.create_batch(10,
                                                         patient=factory.LazyFunction(
                                                             lambda: random.choice(patients)),
                                                         doctor=factory.LazyFunction(
                                                             lambda: random.choice(doctors))
                                                         )

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated database with dummy data'))
