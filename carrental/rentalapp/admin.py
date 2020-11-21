from django.contrib import admin
from .models import Person, Vehicle, Bookings
# Register your models here.

admin.site.register(Person)
admin.site.register(Vehicle)
admin.site.register(Bookings)
