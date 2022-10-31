from django.contrib import admin

from .models import Trip, Driver, Vehicle, Customer

# Register your models here.
admin.site.register(Trip)
admin.site.register(Driver)
admin.site.register(Customer)
admin.site.register(Vehicle)
