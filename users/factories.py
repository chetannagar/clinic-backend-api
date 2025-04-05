import factory
import random
from users.models import User
from faker import Faker

fake = Faker('en_US')

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    firebase_uid = factory.Faker('uuid4')
    email = factory.Faker('email')
    password_hash = factory.Faker('password')  # Or leave blank/null as needed
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    phone_number = factory.LazyFunction(lambda: fake.msisdn()[:10])  # Get 10 digit US phone number
    role = factory.Iterator([
        User.ROLE_PATIENT,
        User.ROLE_DOCTOR,
        User.ROLE_ADMIN,
        User.ROLE_STAFF,
    ])
    specialization = factory.LazyFunction(lambda: fake.job() if random.random() < 0.5 else None)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"