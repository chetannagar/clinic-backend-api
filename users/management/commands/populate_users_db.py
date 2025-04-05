# myapp/management/commands/populate_users_db.py
from django.core.management.base import BaseCommand
from users.factories import UserFactory

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **options):
        users = UserFactory.create_batch(10)

        self.stdout.write(self.style.SUCCESS('Successfully populated database with dummy users data'))