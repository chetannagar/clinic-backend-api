import factory
import random
from payments.models import Payment, Invoice
from patients.factories import PatientFactory
from doctors.factories import DoctorFactory
from appointments.factories import AppointmentFactory
from faker import Faker

fake = Faker()

class PaymentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Payment

    patient = factory.SubFactory(PatientFactory)
    doctor = factory.SubFactory(DoctorFactory)
    appointment = factory.SubFactory(AppointmentFactory)
    amount = factory.LazyFunction(lambda: round(random.uniform(50, 500), 2))
    payment_method = factory.Iterator([
        Payment.PAYMENT_CREDIT_CARD,
        Payment.PAYMENT_DEBIT_CARD,
        Payment.PAYMENT_CASH,
        Payment.PAYMENT_INSURANCE,
    ])
    transaction_status = factory.Iterator([
        Payment.TRANSACTION_STATUS_PENDING,
        Payment.TRANSACTION_STATUS_COMPLETED,
        Payment.TRANSACTION_STATUS_FAILED,
        Payment.TRANSACTION_STATUS_REFUNDED,
    ])
    transaction_id = factory.Faker('uuid4')

class InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Invoice

    patient = factory.SubFactory(PatientFactory)
    appointment = factory.SubFactory(AppointmentFactory)
    total_amount = factory.LazyFunction(lambda: round(random.uniform(50, 500), 2))
    payment_status = factory.Iterator([
        Invoice.PAYMENT_STATUS_PAID,
        Invoice.PAYMENT_STATUS_UNPAID,
        Invoice.PAYMENT_STATUS_REFUNDED,
    ])
    invoice_pdf_url = factory.LazyFunction(lambda: f"https://clinic-invoices.com/{fake.uuid4()}.pdf")