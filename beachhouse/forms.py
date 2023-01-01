from django import forms
from django.forms import ModelForm
from .models import Bookings, House

# form for adding a house


class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = '__all__'

# form for bookings


class BookingForm(ModelForm):
    class Meta:
        model = Bookings
        fields = '__all__'

        labels = {
            'user': '',
            'house': 'Your chosen house',
            'checkin': 'When do you want to check in?',
            'checkout': 'When do you want to check out?',
        }
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'house': forms.TextInput(attrs={'class': 'form-control'}),
            'checkin': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
            'checkout': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
        }
