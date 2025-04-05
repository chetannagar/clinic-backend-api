import factory
import random
import datetime
from django.utils import timezone
from notifications.models import Notification, Message
from users.factories import UserFactory
from appointments.factories import AppointmentFactory


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Notification

    user = factory.SubFactory(UserFactory)
    appointment = factory.Maybe(
        factory.LazyFunction(lambda: random.choice([True, False])),
        yes_declaration=factory.SubFactory(AppointmentFactory),
        no_declaration=None
    )
    type = factory.Iterator([
        Notification.TYPE_SMS,
        Notification.TYPE_EMAIL,
    ])
    status = factory.Iterator([
        Notification.STATUS_PENDING,
        Notification.STATUS_SENT,
        Notification.STATUS_FAILED,
    ])
    sent_at = factory.LazyFunction(lambda: timezone.now() if random.random() < 0.5 else None)


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message

    sender = factory.SubFactory(UserFactory)
    receiver = factory.SubFactory(UserFactory)
    content = factory.Faker('paragraph')
    is_read = factory.LazyFunction(lambda: random.choice([True, False]))

    @factory.lazy_attribute
    def read_at(self):
        if self.is_read:
            return timezone.now()
        return None