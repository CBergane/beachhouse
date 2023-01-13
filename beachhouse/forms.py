from django import forms
from django.forms import ModelForm
from .models import Bookings, House
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core import validators


class HouseForm(ModelForm):
    '''
    Form for adding a house
    '''
    class Meta:
        model = House
        fields = (
            'name',
            'adress',
            'owner',
            'beds',
            'capacity',
            'price',
            'description',
            'house_image',
            )
        labels = {
            'name': '',
            'adress': '',
            'owner': 'Owner of the house',
            'beds': 'Number of beds',
            'capacity': 'Number of guests',
            'price': 'Price per night',
            'description': '',
            'house_image': 'Add a picture of your house',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'House Name'
                }),
            'adress': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'House Adress',
                }),
            'owner': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Owner of the house',
                }),
            'beds': forms.NumberInput(attrs={
                'class': 'form-range',
                'id': 'beds',
                'type': 'range',
                'min': '0',
                'max': '10',
                'placeholder': 'Number of guests',
                }),
            'capacity': forms.NumberInput(attrs={
                'class': 'form-range',
                'id': 'capacity',
                'type': 'range',
                'min': '0',
                'max': '10',
                'placeholder': 'Number of guests',
                }),
            'price': forms.NumberInput,
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the house',
                }),
            'house_image': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
                'placeholder': 'House Name',
                }),
        }


class BookingForm(forms.ModelForm):
    '''
    Form for making a booking
    '''
    class Meta:
        model = Bookings
        fields = ('checkin', 'checkout',)

        labels = {
            'checkin': 'When do you want to check in?',
            'checkout': 'When do you want to check out?',
        }
        widgets = {
            'checkin': forms.DateTimeInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    }
            ),
            'checkout': forms.DateTimeInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    }
            ),
        }
