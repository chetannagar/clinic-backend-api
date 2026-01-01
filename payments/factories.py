import random

import factory
from faker import Faker

from appointments.factories import AppointmentFactory
from payments.models import Invoice, Payment

fake = Faker()

class PaymentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Payment

    appointment = factory.SubFactory(AppointmentFactory)
    patient = factory.LazyAttribute(lambda o: o.appointment.patient if o.appointment else None)
    doctor = factory.LazyAttribute(lambda o: o.appointment.doctor if o.appointment else None)
    amount = factory.LazyFunction(lambda: round(random.uniform(50, 500), 2))
    payment_method = factory.Iterator(
        [
            Payment.PAYMENT_CREDIT_CARD,
            Payment.PAYMENT_DEBIT_CARD,
            Payment.PAYMENT_CASH,
            Payment.PAYMENT_INSURANCE,
        ]
    )
    transaction_status = factory.Iterator(
        [
            Payment.TRANSACTION_STATUS_PENDING,
            Payment.TRANSACTION_STATUS_COMPLETED,
            Payment.TRANSACTION_STATUS_FAILED,
            Payment.TRANSACTION_STATUS_REFUNDED,
        ]
    )
    transaction_id = factory.Faker("uuid4")

class InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Invoice

    appointment = factory.SubFactory(AppointmentFactory)
    patient = factory.LazyAttribute(lambda o: o.appointment.patient if o.appointment else None)
    total_amount = factory.LazyFunction(lambda: round(random.uniform(50, 500), 2))
    payment_status = factory.Iterator(
        [
            Invoice.PAYMENT_STATUS_PAID,
            Invoice.PAYMENT_STATUS_UNPAID,
            Invoice.PAYMENT_STATUS_REFUNDED,
        ]
    )
    invoice_pdf_url = factory.LazyFunction(lambda: f"https://clinic-invoices.com/{fake.uuid4()}.pdf")