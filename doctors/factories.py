import datetime
import random

import factory

from doctors.models import Doctor, DoctorAvailability
from users.factories import UserFactory
from users.models import User

class DoctorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Doctor

    user = factory.SubFactory(UserFactory, role=User.ROLE_DOCTOR)
    license_number = factory.Sequence(lambda n: f"LIC-{n:06d}")
    specialization = factory.Faker('job')
    qualifications = factory.Faker('text', max_nb_chars=200)
    experience = factory.LazyFunction(lambda: random.randint(1, 40))
    consultation_fee = factory.LazyFunction(lambda: round(random.uniform(50, 500), 2))

    def __str__(self):
        return self.user.email
    
class DoctorAvailabilityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DoctorAvailability

    doctor = factory.SubFactory(DoctorFactory)
    day_of_week = factory.Faker('random_element', elements=[day[0] for day in DoctorAvailability.DAYS_OF_WEEK])
    start_time = factory.LazyFunction(lambda: datetime.time(hour=random.randint(8, 16)))
    end_time = factory.LazyAttribute(lambda o: (
    (datetime.datetime.combine(datetime.date.today(), o.start_time) + datetime.timedelta(hours=1)).time()))
    is_available = factory.LazyFunction(lambda: random.choice([True, False]))

    def __str__(self):
        return f"{self.doctor.user.full_name} - {self.day_of_week} ({self.start_time} to {self.end_time})"