# myapp/management/commands/populate_notifications_db.py
from django.core.management.base import BaseCommand
from notifications.factories import NotificationFactory, MessageFactory

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **options):
        notifications = NotificationFactory.create_batch(30)
        messages = MessageFactory.create_batch(20)

        self.stdout.write(self.style.SUCCESS('Successfully populated database with dummy notifications data'))