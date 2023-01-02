from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import House, Bookings
from .forms import BookingForm


# Create your views here.
def base(request):
    return render(request, 'base.html', {})


def index(request):
    return render(request, 'index.html', {})


def house_list(request):
    house_list = House.objects.all()
    return render(request, 'house_list.html', {'house_list': house_list})


# add a booking
def add_booking(request, house_id):
    house = House.objects.get(pk=house_id)
    submitted = False
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.house = house
            obj.save()
            return HttpResponseRedirect('/bookings_list?submitted=True')
    else:
        form = BookingForm

    return render(request, 'add_booking.html', {
        'form': form,
        'submitted': submitted,
        'house': house,
        })
# add_booking?submitted=True


# list your bookings
class BookingList(ListView):
    model = Bookings
    template_name = 'bookings_list.html'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Bookings.objects.all()
            return booking_list
        else:
            booking_list = Bookings.objects.filter(user=self.request.user)
            return booking_list


def booking_list_admin(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    # converting month to numbers
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # print out a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    # Get current year
    now = datetime.now()
    current_year = now.year

    booking_list = Bookings.objects.all()

    return render(request, 'admin/booking_list_admin.html', {
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
        'current_year': current_year,
        'booking_list': booking_list,
    })
