import uuid
import factory
import random
import datetime
from django.utils import timezone
from clinic_settings.models import ClinicSetting, Review, AuditLog, AdminActionLog
from doctors.factories import DoctorFactory
from patients.factories import PatientFactory
from users.factories import UserFactory
from faker import Faker

fake = Faker()

class ClinicSettingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ClinicSetting

    key = factory.Faker('word')
    value = factory.Faker('sentence')


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    # Will ensure unique patient-doctor pair by tracking used pairs
    _used_pairs = set()

    @classmethod
    def _generate(cls, strategy, params):
        attempts = 0
        while attempts < 10:
            patient = PatientFactory()
            doctor = DoctorFactory()
            key = (patient.id, doctor.id)
            if key not in cls._used_pairs:
                cls._used_pairs.add(key)
                params['patient'] = patient
                params['doctor'] = doctor
                break
            attempts += 1
        return super()._generate(strategy, params)

    rating = factory.LazyFunction(lambda: random.randint(1, 5))
    review_text = factory.Faker('paragraph')


class AuditLogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AuditLog

    user = factory.SubFactory(UserFactory)
    action = factory.LazyFunction(lambda: random.choice([
        "Created Appointment",
        "Updated Profile",
        "Cancelled Appointment",
        "Added Prescription",
        "Viewed Patient Record",
        "Edited Availability",
    ]))
    timestamp = factory.LazyFunction(timezone.now)

class AdminActionLogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AdminActionLog

    id = factory.LazyFunction(uuid.uuid4)
    user = factory.SubFactory(UserFactory, role='Admin')  # Only Admins perform actions
    action = factory.LazyFunction(lambda: fake.sentence(nb_words=10))  # Random short description of the action
    created_at = factory.LazyFunction(fake.date_time_this_year)

    def __str__(self):
        return f"{self.user.email} - {self.action}"