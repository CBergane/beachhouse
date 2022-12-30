from django.contrib import admin
from .models import Bookings, House, Owner


admin.site.register(Bookings)
admin.site.register(House)
admin.site.register(Owner)
