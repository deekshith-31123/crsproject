from django.contrib import admin

from .models import Registration, Owner,  Car,Company

# Register your models here.
admin.site.register(Registration)
admin.site.register(Car)
admin.site.register(Company)