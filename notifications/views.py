from django.shortcuts import render
from rest_framework import viewsets
from notifications.models import Notification, Message
from notifications.serializers import NotificationSerializer, MessageSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer