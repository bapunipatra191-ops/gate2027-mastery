from django.contrib import admin
from .models import PremiumUser, ContactMessage, PurchaseRequest

admin.site.register(PremiumUser)
admin.site.register(ContactMessage)
admin.site.register(PurchaseRequest)