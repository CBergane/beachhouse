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
            'beds',
            'capacity',
            'has_tv',
            'has_wifi',
            'has_bbq',
            'has_shower',
            'has_bath',
            'bed_size',
            'price',
            'description',
            'house_image',
            )
        labels = {
            'name': '',
            'adress': '',
            'beds': 'Number of beds',
            'capacity': 'Number of guests',
            'has_tv': 'Tv',
            'has_wifi': 'WiFi',
            'has_bbq': 'Dose it have a grill',
            'has_shower': 'Shower',
            'has_bath': 'Bath',
            'bed_size': 'Bed Size',
            'price': 'Price per night €',
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
            'has_tv': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                }),
            'has_wifi': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                }),
            'has_bbq': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                }),
            'has_shower': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                }),
            'has_bath': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                }),
            'bed_size': forms.Select(attrs={
                'class': 'dropdown-toggle',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 10,
                }),
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


class HouseSearchForm(forms.ModelForm):

    class Meta:
        model = House

        fields = (
            'bed_size',
            'capacity',
            'has_tv',
            'has_wifi',
            'has_bbq',
            'has_shower',
            'has_bath',
        )
        labels = {
            'capacity': 'Number of guests',
            'has_tv': 'Tv',
            'has_wifi': 'WiFi',
            'has_bbq': 'Dose it have a grill',
            'has_shower': 'Shower',
            'has_bath': 'Bath',
            'bed_size': 'Bed Size',
        }
        widgets = {
            'bed_size': forms.Select(attrs={
                'class': 'form-select',
            }),
            'capacity': forms.NumberInput(attrs={
                'class': 'form-range',
                'id': 'capacity',
                'type': 'range',
                'min': '0',
                'max': '10',
                'placeholder': 'Number of guests',
            }),
            'has_tv': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                }),
            'has_wifi': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                }),
            'has_bbq': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                }),
            'has_shower': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                }),
            'has_bath': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                }),
        }
