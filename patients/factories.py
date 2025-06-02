import factory
# import random
from patients.models import Patient
# from users.factories import UserFactory
from faker import Faker

fake = Faker('en_US')

class PatientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Patient

    # Ensure created user has role 'Patient'
    user = None # factory.SubFactory(UserFactory, role='Patient')
    date_of_birth = factory.Faker('date_between', start_date='-80y', end_date='-18y')
    gender = factory.Iterator([
        Patient.GENDER_MALE,
        Patient.GENDER_FEMALE,
        Patient.GENDER_OTHER,
    ])
    address = factory.Faker('address')

    # Format emergency contact as 10-digit US phone number
    emergency_contact = factory.LazyFunction(lambda: fake.msisdn()[:10])

    def __str__(self):
        return self.user.email