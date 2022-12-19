from django.db import models
from django.conf import settings


class Guests(models.Model):
    fname = models.CharField('Guest First Name', max_length=20)
    lname = models.CharField('Guest Last Name', max_length=20)
    email = models.EmailField(('Email Adress'))
    phone = models.CharField('Contact Phone', max_length=15)

    def __str__(self):
        return self.fname + ' ' + self.lname


class House(models.Model):
    name = models.CharField('House Name', max_length=20)
    adress = models.CharField('House Adress', max_length=30)
    owner = models.CharField('House Owner', max_length=30)
    description = models.TextField(blank=True)
    booking = models.ManyToManyField(Guests, blank=True)

    def __str__(self):
        return self.name


class Bookings(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    checkin = models.DateTimeField('Check In')
    checkout = models.DateTimeField('Check Out')

    def __str__(self):
        return self.name
