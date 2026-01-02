from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, MeView, UpdateProfileView, DeleteUserView

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path("me/", MeView.as_view(), name="user-me"),
    path("update/", UpdateProfileView.as_view(), name="user-update"),
    path("delete/", DeleteUserView.as_view(), name="user-delete"),
]
urlpatterns += router.urls
