import uuid
from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    PAYMENT_CREDIT_CARD = 'Credit Card'
    PAYMENT_DEBIT_CARD = 'Debit Card'
    PAYMENT_CASH = 'Cash'
    PAYMENT_INSURANCE = 'Insurance'
    PAYMENT_METHOD_CHOICES = [
        (PAYMENT_CREDIT_CARD, 'Credit Card'),
        (PAYMENT_DEBIT_CARD, 'Debit Card'),
        (PAYMENT_CASH, 'Cash'),
        (PAYMENT_INSURANCE, 'Insurance'),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    TRANSACTION_STATUS_PENDING = 'Pending'
    TRANSACTION_STATUS_COMPLETED = 'Completed'
    TRANSACTION_STATUS_FAILED = 'Failed'
    TRANSACTION_STATUS_REFUNDED = 'Refunded'
    TRANSACTION_STATUS_CHOICES = [
        (TRANSACTION_STATUS_PENDING, 'Pending'),
        (TRANSACTION_STATUS_COMPLETED, 'Completed'),
        (TRANSACTION_STATUS_FAILED, 'Failed'),
        (TRANSACTION_STATUS_REFUNDED, 'Refunded'),
    ]
    transaction_status = models.CharField(max_length=20, choices=TRANSACTION_STATUS_CHOICES)
    transaction_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment for {self.patient.user.email}"
    
class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    PAYMENT_STATUS_PAID = 'Paid'
    PAYMENT_STATUS_UNPAID = 'Unpaid'
    PAYMENT_STATUS_REFUNDED = 'Refunded'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PAID, 'Paid'),
        (PAYMENT_STATUS_UNPAID, 'Unpaid'),
        (PAYMENT_STATUS_REFUNDED, 'Refunded'),
    ]
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    invoice_pdf_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice for {self.patient.user.email}"