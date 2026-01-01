import uuid
from django.db import models
from users.models import User
from appointments.models import Appointment

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    TYPE_SMS = 'SMS'
    TYPE_EMAIL = 'Email'
    TYPE_CHOICES = [
        (TYPE_SMS, 'SMS'),
        (TYPE_EMAIL, 'Email'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    STATUS_PENDING = 'Pending'
    STATUS_SENT = 'Sent'
    STATUS_FAILED = 'Failed'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_SENT, 'Sent'),
        (STATUS_FAILED, 'Failed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    provider_message_id = models.CharField(max_length=255, blank=True)
    error_message = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(blank=True, null=True)
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Notification to {self.user.email or 'Unknown'}"
    
    class Meta:
        ordering = ['-created_at']
    
class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Message from {self.sender.email} to {self.receiver.email}"