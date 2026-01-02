from django.urls import path
from payments.views import InvoiceGenerateView, InvoiceDetailView

urlpatterns = [
    path("generate/", InvoiceGenerateView.as_view(), name="invoice-generate"),
    path("<uuid:pk>/", InvoiceDetailView.as_view(), name="invoice-detail"),
]
