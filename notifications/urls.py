from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notifications.views import (
    NotificationViewSet,
    MessageViewSet,
    NotificationSendView,
    NotificationListView,
    NotificationDetailView,
    NotificationReadView,
)

router = DefaultRouter()
router.register(r'', NotificationViewSet, basename='notification')
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path("send/", NotificationSendView.as_view(), name="notification-send"),
    path("list/", NotificationListView.as_view(), name="notification-list"),
    path("<uuid:pk>/", NotificationDetailView.as_view(), name="notification-detail"),
    path("<uuid:pk>/read/", NotificationReadView.as_view(), name="notification-read"),
]
urlpatterns += router.urls
