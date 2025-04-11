# myapp/management/commands/populate_appointment_db.py
from django.core.management.base import BaseCommand
from appointments.factories import AppointmentFactory


class Command(BaseCommand):
    """Command to populate the database with dummy appointment data."""
    help = "Populates the database with dummy data"

    def handle(self, *args, **options):
        appointments = AppointmentFactory.create_batch(20)

        self.stdout.write(
            self.style.SUCCESS("Successfully populated database with dummy appointments data") # pylint: disable=no-member
        )
