import uuid
import factory
import random
from django.utils import timezone
from clinic_settings.models import AdminActionLog, AuditLog, ClinicSetting, Review
from doctors.factories import DoctorFactory
from patients.factories import PatientFactory
from users.factories import UserFactory
from faker import Faker

fake = Faker()


class ClinicSettingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ClinicSetting

    key = factory.Sequence(lambda n: f"setting_{n}")
    value = factory.Faker("sentence")


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    patient = factory.SubFactory(PatientFactory)
    doctor = factory.SubFactory(DoctorFactory)
    rating = factory.LazyFunction(lambda: random.randint(1, 5))
    review_text = factory.Faker("paragraph")


class AuditLogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AuditLog

    user = factory.SubFactory(UserFactory)
    action = factory.LazyFunction(
        lambda: random.choice(
            [
                "Created Appointment",
                "Updated Profile",
                "Cancelled Appointment",
                "Added Prescription",
                "Viewed Patient Record",
                "Edited Availability",
            ]
        )
    )
    timestamp = factory.LazyFunction(timezone.now)


class AdminActionLogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AdminActionLog

    id = factory.LazyFunction(uuid.uuid4)
    user = factory.SubFactory(UserFactory, role="Admin")  # Only Admins perform actions
    action = factory.LazyFunction(
        lambda: fake.sentence(nb_words=10)
    )  # Random short description of the action
    created_at = factory.LazyFunction(fake.date_time_this_year)

    def __str__(self):
        return f"{self.user.email} - {self.action}"
