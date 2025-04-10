import factory
from users.models import User
from faker import Faker
import uuid

fake = Faker('en_US')

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.LazyFunction(uuid.uuid4)
    firebase_uid = factory.LazyFunction(uuid.uuid4)
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
    # created_at = factory.Faker('date_time_this_decade')
    # updated_at = factory.Faker('date_time_this_decade')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"