from django.shortcuts import render, redirect, get_object_or_404
import calendar
from calendar import HTMLCalendar
from datetime import datetime, timedelta
from django.db.models import Q
from django.http import (
    HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseNotFound
    )
from django.views.generic import ListView, View
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import House, Bookings, Contact
from .forms import BookingForm, HouseForm, HouseSearchForm, ContactForm
from beachhouse.booking.booking_function import check_availability


def base(request):
    '''
    Base template the holds everything together
    '''
    return render(request, 'base.html', {})


def index(request):
    '''
    Renders the main page/home page and a contact form
    '''
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your message has been sent.')
            message = form.save()
        else:
            messages.error(request, 'Your message was not sent.')
    return render(request, 'index.html', {'form': form})


def house_list(request):
    '''
    List all houses in the database
    '''
    house_list = House.objects.all()
    beds = request.GET.get('beds')
    has_wifi = request.GET.get('has_wifi')
    has_tv = request.GET.get('has_tv')
    has_bbq = request.GET.get('has_bbq')
    has_shower = request.GET.get('has_shower')
    has_bath = request.GET.get('has_bath')
    capacity = request.GET.get('capacity')
    if beds:
        house_list = house_list.filter(beds=beds)
    if has_wifi:
        house_list = house_list.filter(has_wifi=True)
    if has_tv:
        house_list = house_list.filter(has_tv=True)
    if has_bbq:
        house_list = house_list.filter(has_bbq=True)
    if has_shower:
        house_list = house_list.filter(has_shower=True)
    if has_bath:
        house_list = house_list.filter(has_bath=True)
    if capacity:
        house_list = house_list.filter(capacity__gte=capacity)
    return render(request, 'house_list.html', {'house_list': house_list})


class AddBooking(View):
    '''
    Booking function to check if a house is not booked
    if it is not booked then book it
    '''
    def get(self, request, *args, **kwargs):
        house_name = self.kwargs.get('house_id', None)
        form = BookingForm()
        house_list = House.objects.filter(id=house_name)
        if len(house_list) > 0:
            house = house_list[0]
            house_owner = User.objects.get(pk=house.owner)
            obj = House.objects.get(id=house_name)
            context = {
                'house_name': house_name,
                'form': form,
                'obj': obj,
                'house_owner': house_owner,
            }
        return render(request, 'add_booking.html', context)

    def post(self, request, *args, **kwargs):
        '''
        Posting the booking and if the form is approved,
        then save it else try again
        '''
        house_name = self.kwargs.get('house_id', None)
        house_list = House.objects.filter(id=house_name)
        form = BookingForm(request.POST)
        available_house = []
        house = ''

        if form.is_valid():
            data = form.cleaned_data
            for house in house_list:
                if check_availability(
                    house, data['checkin'], data['checkout']
                        ):
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

        @csrf_exempt
        def calculate_cost(self, request):
            '''
            adding a way to calculate the total cost
            of the booking as you chose days
            '''
            checkin = request.POST.get('checkin')
            checkout = request.POST.get('checkout')
            house_id = request.POST.get('house_id')
            house = House.objects.get(pk=house_id)
            delta = datetime.strptime(
                checkout, '%Y-%m-%d') - datetime.strptime(checkin, '%Y-%m-%d')
            days = delta.days
            cost = days * house.rate
        return JsonResponse({'total_cost': cost})


class BookingList(ListView):
    '''
    List all bookings with total cost
    '''
    model = Bookings
    template_name = 'bookings_list.html'

    def get_queryset(self):
        # Retrieve the existing bookings from the database
        bookings = super().get_queryset().filter(user=self.request.user)
        for booking in bookings:
            checkin = booking.checkin
            checkout = booking.checkout
            house = booking.house
            rate = house.price

            # Calculate the number of days between
            # the check-in and check-out dates
            delta = checkout - checkin
            days = delta.days

            # Use the number of days to calculate the price of the booking
            booking.price = days * rate
        return bookings

    def get(self, request, *args, **kwargs):
        bookings = self.get_queryset()
        houses = House.objects.filter(owner=self.request.user.pk)
        context = {
            'bookings': bookings,
            'houses': houses,
        }
        for booking in bookings:
            house_owner = User.objects.get(pk=booking.house.owner)
            context['house_owner'] = house_owner
        return render(request, self.template_name, context)


def bookings_update(request, bookings_id):
    '''
    Uppdate a existing booking
    '''
    booking = Bookings.objects.get(pk=bookings_id)
    form = BookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        checkin = form.cleaned_data['checkin']
        checkout = form.cleaned_data['checkout']
        conflicting_bookings = Bookings.objects.filter(
            checkin__lte=checkout,
            checkout__gte=checkin).exclude(pk=bookings_id)
        if conflicting_bookings.exists():
            # If any conflicting bookings are found,
            # return an error message to the user
            messages.error(
                request, 'A booking exist already, try another one.'
                )
            return render(request, 'bookings_update.html', {
                'form': form,
                'booking': booking,
                })
        else:
            form.save()
        return redirect('BookingList')
    return render(request, 'bookings_update.html', {
        'booking': booking,
        'form': form,
        })


def bookings_delete(request, bookings_id):
    '''
    Delete a booking
    '''
    booking = Bookings.objects.get(pk=bookings_id)
    if request.user == booking.user:
        booking.delete()
        messages.success(request, ('Your booking has been deleted'))
        return redirect('BookingList')
    else:
        messages.success(request, ('You dont have authorization to do this'))
        return redirect('BookingList')


def add_house(request):
    '''
    Users can add houses
    '''
    submitted = False
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Your house has been added')
            house = form.save(commit=False)
            house.owner = request.user.id  # request the users id
            house.save()
            return HttpResponseRedirect('add_house?submitted=True')
    else:
        form = HouseForm
        if submitted in request.GET:
            submitted = True

    return render(request, 'add_house.html', {
        'form': form,
        'submitted': submitted,
        })


def house_update(request, house_id):
    '''
    Uppdate a house if you have acces
    '''
    house = House.objects.get(pk=house_id)
    form = HouseForm(request.POST or None, instance=house)
    if form.is_valid():
        messages.success(request, 'Your house has been updated.')
        form.save()
        return redirect('house-list')
    return render(request, 'house_update.html', {'house': house, 'form': form})


def house_delete(request, house_id):
    '''
    Delete a house from the database
    '''
    house = House.objects.get(pk=house_id)
    house.delete()
    return redirect('house-list')


def booking_list_admin(
    request, year=datetime.now().year,
    month=datetime.now().strftime('%B')
        ):
    '''
    The admin template where all the bookings are displayed and
    the messages from the index page ends up at
    '''
    message = Contact.objects.all()
    num_messages = Contact.objects.count()
    if request.user.is_superuser:
        month = month.capitalize()
        # converting month to numbers
        month_number = list(calendar.month_name).index(month)
        month_number = int(month_number)

        # print out a calendar
        cal = HTMLCalendar().formatmonth(year, month_number)

        # Get current year
        now = datetime.now()
        current_year = now.year

        # showing the uppcoming bookings
        booking_list = Bookings.objects.filter(
            checkin__year=year,
            checkin__month=month_number,
        )

        # display houses that need to be approved befor shown on the page
        house_list = House.objects.all().order_by('name')

        if request.method == 'GET':
            year = int(request.GET.get('year', datetime.now().year))
            month = request.GET.get('month', datetime.now().strftime('%B'))
            month = month.capitalize()
            month_number = list(calendar.month_name).index(month)
            month_number = int(month_number)
            if 'prev' in request.GET:
                month_number = month_number - 1 if month_number > 1 else 12
                month = calendar.month_name[month_number]
            elif 'next' in request.GET:
                month_number = month_number + 1 if month_number < 12 else 1
                month = calendar.month_name[month_number]
            booking_list = Bookings.objects.filter(
                checkin__year=year,
                checkin__month=month_number,
            )
            return render(request, 'admin/booking_list_admin.html', {
                'year': year,
                'month': month,
                'month_number': month_number,
                'cal': cal,
                'current_year': current_year,
                'booking_list': booking_list,
                'house_list': house_list,
                'now': now,
                'message': message,
                'num_messages': num_messages,
                })

        if request.method == 'POST':
            id_list = request.POST.getlist('boxes')

            house_list.update(approved=False)

            # update the database to approve the checkboxes
            for box in id_list:
                House.objects.filter(pk=int(box)).update(approved=True)

            messages.success(request, 'House list has been updated')
            return redirect('bookinglistadmin')
        else:
            return render(request, 'admin/booking_list_admin.html', {
                'year': year,
                'month': month,
                'month_number': month_number,
                'cal': cal,
                'current_year': current_year,
                'booking_list': booking_list,
                'house_list': house_list,
                'now': now,
                'message': message,
                'num_messages': num_messages,
            })
        return render(request, 'admin/booking_list_admin.html', {
            'year': year,
            'month': month,
            'month_number': month_number,
            'cal': cal,
            'current_year': current_year,
            'booking_list': booking_list,
            'house_list': house_list,
            'now': now,
            'message': message,
            'num_messages': num_messages,
        })
    else:
        messages.success(request, "You don't have acces to this page")
        return redirect('home')


def message_delete(request, message_id):
    '''
    Delete a message
    '''
    if request.user.is_staff:
        message = Contact.objects.get(pk=message_id)
        message.delete()
        messages.success(request, ('The message has been deleted'))
    return redirect('bookinglistadmin')


def checkout_booking(request, bookings_id):
    '''
    Add a checkout function simular to the delete function for
    the admin to handle bookings
    '''
    if request.user.is_staff:
        booking = Bookings.objects.get(pk=bookings_id)
        booking.delete()
        messages.success(request, 'Booking has been checked out')
    return redirect('bookinglistadmin')


def house_detail(request, pk):
    '''
    Getting a preview of the houses for the admin
    '''
    house = get_object_or_404(House, pk=pk)
    return render(request, 'house_detail.html', {'house': house})


def custom_404(request, exception):
    '''
    A custom made 404
    '''
    return render(request, '404.html')
