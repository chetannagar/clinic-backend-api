# myapp/management/commands/populate_payments_db.py
from django.core.management.base import BaseCommand
from payments.factories import PaymentFactory, InvoiceFactory

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **options):
        payments = PaymentFactory.create_batch(10)
        invoices = InvoiceFactory.create_batch(10)

        self.stdout.write(self.style.SUCCESS('Successfully populated database with dummy payments data'))