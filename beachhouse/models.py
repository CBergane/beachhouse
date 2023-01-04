from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.utils import timezone


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
    house_image = CloudinaryField('image', default='placeholder')

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

    """
    Function to validate date so that
    checkin and checkout date is not in the past.
    """
    def check_in_validate(checkin):
        if checkin < timezone.now():
            raise ValidationError('You cant checkin in the past')
    checkin = models.DateTimeField(null=True, blank=True, validators=[check_in_validate])

    def check_out_validate(checkout):
        if checkout < timezone.now():
            raise ValidationError('You cant checkout in the past')
    checkout = models.DateTimeField(null=True, blank=True, validators=[check_out_validate])

    def __str__(self):
        """
        Function to return object model
        items as string.
        """
        return f'{self.user} has booked {self.house} '
        f'from {self.checkin} untill {self.checkout}'
