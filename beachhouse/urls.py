from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import BookingList, AddBooking

urlpatterns = [
    path('', views.base, name='base'),
    path('index', views.index, name='index'),
    path(
        'house_list',
        views.house_list,
        name='house-list'),
    path(
        'add_booking/<house_id>',
        login_required(AddBooking.as_view()),
        name='add-booking'),
    path(
        'bookings_update/<bookings_id>',
        login_required(views.bookings_update),
        name='bookings-update'),
    path(
        'bookings_delete/<bookings_id>',
        login_required(views.bookings_delete),
        name='bookings-delete'),
    path(
        'bookings_list',
        login_required(BookingList.as_view()),
        name='BookingList'),
    path(
        'search_house',
        views.search_house,
        name='search-house'),
    path(
        'add_house',
        login_required(views.add_house),
        name='add-house'),
    path(
        'house_update/<house_id>',
        login_required(views.house_update),
        name='house-update'),
    path(
        'house_delete/<house_id>',
        login_required(views.house_delete),
        name='house-delete'),
    path(
        'bookinglistadmin',
        login_required(views.booking_list_admin),
        name='bookinglistadmin'),
    path(
        '<int:year>/<str:month>',
        views.booking_list_admin,
        name='bookinglistadmin'),
        ]
