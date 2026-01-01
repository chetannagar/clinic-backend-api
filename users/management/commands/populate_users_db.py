# myapp/management/commands/populate_users_db.py
from django.core.management.base import BaseCommand

from users.factories import UserFactory
from users.models import User

DEFAULT_PATIENT_COUNT = 30
DEFAULT_DOCTOR_COUNT = 10
DEFAULT_ADMIN_COUNT = 5
DEFAULT_STAFF_COUNT = 5

class Command(BaseCommand):
    """Django management command to populate the database with dummy users data."""
    help = "Populates the database with dummy users data."

    def handle(self, *args, **options):
        patient_users = UserFactory.create_batch(DEFAULT_PATIENT_COUNT, role=User.ROLE_PATIENT)
        doctor_users = UserFactory.create_batch(DEFAULT_DOCTOR_COUNT, role=User.ROLE_DOCTOR)
        admin_users = UserFactory.create_batch(DEFAULT_ADMIN_COUNT, role=User.ROLE_ADMIN)
        staff_users = UserFactory.create_batch(DEFAULT_STAFF_COUNT, role=User.ROLE_STAFF)

        total_users = len(patient_users) + len(doctor_users) + len(admin_users) + len(staff_users)

        self.stdout.write(self.style.SUCCESS(f"Successfully populated database with {total_users} dummy users"))