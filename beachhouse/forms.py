from django import forms
from django.forms import ModelForm
from .models import Bookings, House, Message
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
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


class CustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(
            max_length=30, widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Username',
                }))
        self.fields['email'] = forms.EmailField(
            label='Email Address', required=True, widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email address',
                    'autofocus': 'autofocus',
                }))
        self.fields['first_name'] = forms.CharField(
            max_length=30, label='First Name', required=True,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control'
                }))
        self.fields['last_name'] = forms.CharField(
            max_length=30, label='Last Name', required=True,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control'
                }))
        self.fields['password1'] = forms.CharField(
            label='Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                }
            ))
        self.fields['password2'] = forms.CharField(
            label='Password(again)',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                }
            ))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class ContactForm(forms.ModelForm):

    class Meta:
        model = Message

        fields = (
            'fname',
            'lname',
            'email',
            'phone',
            'message'
            )

        lables = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'email': 'E-mail',
            'phone': 'Phonenumber',
            'message': 'Message',
        }

        widgets = {
            'fname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
                }),
            'lname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
                }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail',
                }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone-number',
                }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                }),
        }
