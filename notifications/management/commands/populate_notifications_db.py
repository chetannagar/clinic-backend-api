# myapp/management/commands/populate_notifications_db.py
import random

from django.core.management.base import BaseCommand

from appointments.models import Appointment
from notifications.factories import MessageFactory, NotificationFactory
from users.factories import UserFactory
from users.models import User

DEFAULT_NOTIFICATION_COUNT = 30
DEFAULT_MESSAGE_COUNT = 20

class Command(BaseCommand):
    """Django management command to populate the database with dummy notifications and messages data."""
    help = "Populates the database with dummy notifications and messages data"

    def handle(self, *args, **options):
        users = list(User.objects.all())
        if len(users) < 2:
            # Ensure we have at least two users to exchange messages.
            users.extend(UserFactory.create_batch(2 - len(users)))

        appointments = list(Appointment.objects.all())

        notifications = []
        for _ in range(DEFAULT_NOTIFICATION_COUNT):
            user = random.choice(users)
            appointment = random.choice(appointments) if appointments else None
            notifications.append(NotificationFactory(user=user, appointment=appointment))

        messages = []
        for _ in range(DEFAULT_MESSAGE_COUNT):
            sender = random.choice(users)
            receivers = [u for u in users if u != sender]
            receiver = random.choice(receivers) if receivers else UserFactory()
            messages.append(MessageFactory(sender=sender, receiver=receiver))

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully populated {len(notifications)} notifications and {len(messages)} messages"
            )
        )