# myapp/management/commands/populate_reports_db.py
from django.core.management.base import BaseCommand
from reports.factories import MedicalReportFactory, PrescriptionFactory

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **options):
        medical_reports = MedicalReportFactory.create_batch(10)
        prescriptions = PrescriptionFactory.create_batch(10)

        self.stdout.write(self.style.SUCCESS('Successfully populated database with dummy reports data'))