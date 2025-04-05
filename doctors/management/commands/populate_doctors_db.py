# myapp/management/commands/populate_doctors_db.py
from django.core.management.base import BaseCommand
from doctors.factories import DoctorFactory

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **options):
        doctors = DoctorFactory.create_batch(5)

        self.stdout.write(self.style.SUCCESS('Successfully populated database with dummy doctors data'))