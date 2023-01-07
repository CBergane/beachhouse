from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, View
from django.contrib import messages
from .models import House, Bookings
from .forms import BookingForm, HouseForm
from beachhouse.booking.booking_function import check_availability


# Create your views here.
def base(request):
    return render(request, 'base.html', {})


def index(request):
    return render(request, 'index.html', {})

# List all the houses
def house_list(request):
    house_list = House.objects.all()
    return render(request, 'house_list.html', {'house_list': house_list})


'''
Booking function to check if a house is not booked
if it is not booked then book it
'''

class AddBooking(View):
    def get(self, request, *args, **kwargs):
        house_name = self.kwargs.get('house_id', None)
        form = BookingForm()
        house_list = House.objects.filter(id=house_name)
        if len(house_list) > 0:
            house = house_list[0]
            obj = House.objects.get(id=house_name)
            context = {
                'house_name': house_name,
                'form': form,
                'obj': obj,
            }
        return render(request, 'add_booking.html', context)

    def post(self, request, *args, **kwargs):
        house_name = self.kwargs.get('house_id', None)
        house_list = House.objects.filter(id=house_name)
        form = BookingForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
        available_house = []
        for house in house_list:
            if check_availability(house, data['checkin'], data['checkout']):
                available_house.append(house)
        if len(available_house) > 0:
            house = available_house[0]
            booking = Bookings.objects.create(
                user=self.request.user,
                house=house,
                checkin=data['checkin'],
                checkout=data['checkout']
            )
            booking.save()
            messages.success(request, 'Your booking has been added')
            return HttpResponseRedirect('/bookings_list')
        else:
            messages.error(request, 'Cant book this dates, try another.')
            form = BookingForm()
        return render(
            request=request,
            template_name='add_booking.html',
            context={
                'form': form,
                'house_name': house_name,
                'obj': house,
                }
        )   


# list your bookings
class BookingList(ListView):
    model = Bookings
    template_name = 'bookings_list.html'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Bookings.objects.all().order_by('checkin')
            return booking_list
        else:
            booking_list = Bookings.objects.filter(user=self.request.user)
            return booking_list

# Search house on name
def search_house(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        house = House.objects.filter(name__contains=searched)
        return render(request, 'search_house.html', {'searched': searched, 'house': house, })
    else:
        return render(request, 'search_house.html', {})

# Uppdate a booking
def bookings_update(request, bookings_id):
    booking = Bookings.objects.get(pk=bookings_id)
    form = BookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        form.save()
        return redirect('BookingList')
    return render(request, 'bookings_update.html', {'booking': booking, 'form': form})

# Delete a booking
def bookings_delete(request, bookings_id):
    booking = Bookings.objects.get(pk=bookings_id)
    booking.delete()
    return redirect('BookingList')

# Add a house if you have staff privilages
def add_house(request):
    submitted = False
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Your house has been added')
            form.save()
            return HttpResponseRedirect('add_house?submitted=True')
    else:
        form = HouseForm
        if submitted in request.GET:
            submitted = True
    
    return render(request, 'add_house.html', {'form': form, 'submitted': submitted})

# Update a house
def house_update(request, house_id):
    house = House.objects.get(pk=house_id)
    form = HouseForm(request.POST or None, instance=house)
    if form.is_valid():
        messages.success(request, 'Your house has been updated.')
        form.save()
        return redirect('houselist')
    return render(request, 'house_update.html', {'house': house, 'form': form})

# Delete a house
def house_delete(request, house_id):
    house = House.objects.get(pk=house_id)
    house.delete()
    return redirect('house-list')

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
