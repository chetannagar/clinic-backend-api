import uuid

import factory
from faker import Faker

from users.models import User

fake = Faker("en_US")

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.LazyFunction(uuid.uuid4)
    firebase_uid = factory.LazyFunction(lambda: f"uid-{uuid.uuid4()}")
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    phone_number = factory.LazyFunction(lambda: fake.msisdn()[:10])
    role = factory.Iterator(
        [
            User.ROLE_PATIENT,
            User.ROLE_DOCTOR,
            User.ROLE_ADMIN,
            User.ROLE_STAFF,
        ]
    )
    is_staff = factory.LazyAttribute(lambda obj: obj.role in [User.ROLE_STAFF, User.ROLE_ADMIN])

    @factory.post_generation
    def password(self, create, extracted, **kwargs):  # pylint: disable=unused-argument
        # Always set a usable password; allow override via password parameter.
        raw_password = extracted or "Passw0rd!"
        self.set_password(raw_password)
        if create:
            self.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"
