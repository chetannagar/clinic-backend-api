# myapp/management/commands/populate_patients_db.py
from django.core.management.base import BaseCommand
from patients.factories import PatientFactory

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **options):
        patients = PatientFactory.create_batch(5)

        self.stdout.write(self.style.SUCCESS('Successfully populated database with dummy patients data'))