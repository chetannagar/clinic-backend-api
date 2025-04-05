import factory
import random
import datetime
from django.utils import timezone
from clinic_settings.models import Availability, ClinicSetting, Review, AuditLog
from doctors.factories import DoctorFactory
from patients.factories import PatientFactory
from users.factories import UserFactory
from faker import Faker

fake = Faker()


class AvailabilityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Availability

    doctor = factory.SubFactory(DoctorFactory)
    date = factory.Faker('future_date')

    @staticmethod
    def generate_time_slots():
        slots = []
        start_hour = random.randint(8, 10)
        end_hour = random.randint(16, 18)
        for hour in range(start_hour, end_hour):
            slots.append({
                'start': f"{hour:02d}:00",
                'end': f"{hour + 1:02d}:00"
            })
        return slots

    time_slots = factory.LazyFunction(generate_time_slots)
    is_available = factory.LazyFunction(lambda: random.choice([True, False]))


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