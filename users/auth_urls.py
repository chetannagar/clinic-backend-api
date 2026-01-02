from django.urls import path
from users.views import RegisterPatientView, RegisterDoctorView, LoginView

urlpatterns = [
    path("register/", RegisterPatientView.as_view(), name="auth-register"),
    path("register/doctor/", RegisterDoctorView.as_view(), name="auth-register-doctor"),
    path("login/", LoginView.as_view(), name="auth-login"),
]
