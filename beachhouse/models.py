from django.db import models
from django.conf import settings


class Owner(models.Model):
    fname = models.CharField('Owner First Name', max_length=20)
    lname = models.CharField('Owner Last Name', max_length=20)
    email = models.EmailField(('Email Adress'))
    phone = models.CharField('Contact Phone', max_length=15)

    def __str__(self):
        return self.fname + ' ' + self.lname


class House(models.Model):
    name = models.CharField('House Name', max_length=20)
    adress = models.CharField('House Adress', max_length=30)
    owner = models.ForeignKey(Owner, null=True, on_delete=models.CASCADE)
    beds = models.IntegerField('Number Of Beds', default=0)
    capacity = models.IntegerField('Number Of Guets', default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Bookings(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True, null=True, on_delete=models.CASCADE)
    house = models.ForeignKey(
        House, blank=True, null=True, on_delete=models.CASCADE)
    checkin = models.DateTimeField('Check In')
    checkout = models.DateTimeField('Check Out')

    def __str__(self):
        return f'{self.user} has booked {self.house} '
        f'from {self.check_in} untill {self.check_out}'
