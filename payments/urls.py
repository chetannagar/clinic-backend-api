from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payments.views import (
    PaymentViewSet,
    InvoiceViewSet,
    PaymentChargeView,
    PaymentHistoryView,
    PaymentDetailView,
)

router = DefaultRouter()
router.register(r'', PaymentViewSet, basename='payment')  
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path("charge/", PaymentChargeView.as_view(), name="payment-charge"),
    path("history/", PaymentHistoryView.as_view(), name="payment-history"),
    path("<uuid:pk>/", PaymentDetailView.as_view(), name="payment-detail"),
]
urlpatterns += router.urls
