from django.contrib import admin
from .models import Borrower, Lender, Vehicle, Bookings
# Register your models here.

admin.site.register(Borrower)
admin.site.register(Lender)
admin.site.register(Vehicle)
admin.site.register(Bookings)
