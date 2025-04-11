# myapp/management/commands/populate_clinic_settings_db.py
from django.core.management.base import BaseCommand
from clinic_settings.factories import (
    ClinicSettingFactory,
    ReviewFactory,
    AuditLogFactory,
    AdminActionLogFactory
)


class Command(BaseCommand):
    """Command to populate the database with dummy clinic settings data."""
    help = "Populates the database with dummy data"

    def handle(self, *args, **options):
        clinic_settings = ClinicSettingFactory.create_batch(3)
        reviews = ReviewFactory.create_batch(15)
        audit_logs = AuditLogFactory.create_batch(20)
        admin_action_log = AdminActionLogFactory.create_batch(10)

        self.stdout.write(
            self.style.SUCCESS("Successfully populated database with dummy clinic settings data") # pylint: disable=no-member
        )
