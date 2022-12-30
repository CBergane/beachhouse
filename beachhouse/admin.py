from django.contrib import admin
from .models import Bookings, House, Owner


admin.site.register(Owner)

# custum made admin outlook


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'adress', 'owner')
    ordering = ('name',)
    search_fields = ('name', 'adress')


@admin.register(Bookings)
class BookingAdmin(admin.ModelAdmin):
    fields = (('user', 'house'), 'checkin', 'checkout')
    list_display = ('user', 'checkin', 'checkout')
    list_filter = ('checkin', 'house')
    ordering = ('checkin',)
