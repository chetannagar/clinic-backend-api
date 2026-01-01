import factory

from faker import Faker

from patients.models import Patient
from users.factories import UserFactory
from users.models import User

fake = Faker("en_US")

class PatientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Patient

    user = factory.SubFactory(UserFactory, role=User.ROLE_PATIENT)
    date_of_birth = factory.Faker("date_between", start_date="-80y", end_date="-18y")
    gender = factory.Iterator(
        [
            Patient.GENDER_MALE,
            Patient.GENDER_FEMALE,
            Patient.GENDER_OTHER,
        ]
    )
    address = factory.Faker("address")
    emergency_contact = factory.LazyFunction(lambda: fake.msisdn()[:10])

    def __str__(self):
        return self.user.email