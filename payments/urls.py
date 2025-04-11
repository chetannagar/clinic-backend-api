from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payments.views import PaymentViewSet, InvoiceViewSet

router = DefaultRouter()
router.register(r'', PaymentViewSet, basename='payment')  
router.register(r'invoices', InvoiceViewSet)

urlpatterns = router.urls
