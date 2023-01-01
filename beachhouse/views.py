from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import House
from .forms import BookingForm

# Create your views here.


def base(request):
    return render(request, 'base.html', {})


def index(request):
    return render(request, 'index.html', {})


def house_list(request):
    house_list = House.objects.all()
    return render(request, 'house_list.html', {'house_list': house_list})


def add_booking(request):
    submitted = False
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_booking?submitted=True')
    else:
        form = BookingForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_booking.html', {
        'form': form,
        'submitted': submitted,
        })


def booking_list_admin(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    user = 'admin'
    month = month.capitalize()
    # converting month to numbers
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # print out a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    # Get current year
    now = datetime.now()
    current_year = now.year

    return render(request, 'admin/booking_list_admin.html', {
        'user': user,
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
        'current_year': current_year,
    })
