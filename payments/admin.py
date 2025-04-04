from django.contrib import admin
from payments.models import Payment, Invoice

admin.site.register(Payment)
admin.site.register(Invoice)