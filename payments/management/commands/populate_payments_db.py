# myapp/management/commands/populate_payments_db.py
import random

from django.core.management.base import BaseCommand

from appointments.factories import AppointmentFactory
from appointments.models import Appointment
from payments.factories import InvoiceFactory, PaymentFactory

DEFAULT_PAYMENT_COUNT = 10
DEFAULT_INVOICE_COUNT = 10

class Command(BaseCommand):
    """Django management command to populate the database with dummy payments and invoices data."""
    help = "Populates the database with dummy payments and invoices data"

    def handle(self, *args, **options):
        appointments = list(Appointment.objects.all())
        if not appointments:
            appointments = list(AppointmentFactory.create_batch(DEFAULT_PAYMENT_COUNT))

        payments = [
            PaymentFactory(appointment=random.choice(appointments))
            for _ in range(DEFAULT_PAYMENT_COUNT)
        ]

        invoices = [
            InvoiceFactory(appointment=random.choice(appointments))
            for _ in range(DEFAULT_INVOICE_COUNT)
        ]

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully populated {len(payments)} payments and {len(invoices)} invoices"
            )
        )