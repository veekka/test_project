from django.contrib import admin
from .models import Product, Manufacturer, CreditApplication, Contract


admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Contract)
admin.site.register(CreditApplication)

