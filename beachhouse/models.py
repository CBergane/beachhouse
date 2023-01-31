from django.db import models
from django import forms
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.urls import reverse
import pytz
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class Contact(models.Model):
    fname = models.CharField('First Name', max_length=20)
    lname = models.CharField('Last Name', max_length=20)
    email = models.EmailField(('Email Adress'))
    phone = models.CharField('Phone number', max_length=15)
    message = models.CharField('Message', max_length=300, blank=False)

    def __str__(self):
        return self.message


class House(models.Model):
    name = models.CharField('House Name', max_length=20)
    adress = models.CharField('House Adress', max_length=30)
    owner = models.IntegerField('House Owner', blank=False, default=1)
    beds = models.IntegerField('Number Of Beds', default=0)
    capacity = models.IntegerField('Number Of Guests', default=0)
    price = models.IntegerField('Price Per Night', default=0)
    description = models.TextField(blank=True)
    house_image = CloudinaryField('image', default='placeholder')
    has_tv = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    has_bbq = models.BooleanField(default=False)
    has_shower = models.BooleanField(default=False)
    has_bath = models.BooleanField(default=False)
    BED_SIZE_CHOICES = [
        ('S', 'Single'),
        ('D', 'Double'),
        ('Q', 'Queen'),
        ('K', 'King'),
    ]
    bed_size = models.CharField(
        max_length=1,
        choices=BED_SIZE_CHOICES,
        default='D',
    )
    approved = models.BooleanField('Approved', default=False)

    def get_absolute_url(self):
        return reverse('house-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Bookings(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True, null=True, on_delete=models.CASCADE)
    house = models.ForeignKey(
        House, blank=True, null=True, on_delete=models.CASCADE)
    checkin = models.DateTimeField(
        validators=[MinValueValidator(
            datetime.datetime.now().replace(tzinfo=pytz.UTC)
            )])
    checkout = models.DateTimeField(
        validators=[MinValueValidator(
            datetime.datetime.now().replace(tzinfo=pytz.UTC)
            )])

    def __str__(self):
        """
        Function to return object model
        items as string.
        """
        return f'{self.user} has booked {self.house} '
        f'from {self.checkin} untill {self.checkout}'
