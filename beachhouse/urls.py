from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import BookingList, AddBooking

urlpatterns = [
    path('', views.base, name='base'),
    path('index', views.index, name='index'),
    path('houselist', views.house_list, name='houselist'),
    path('add_booking/<house_id>', login_required(AddBooking.as_view()), name='add-booking'),
    path('bookings_update/<bookings_id>', login_required(views.bookings_update), name='bookings-update'),
    path('bookings_list', login_required(BookingList.as_view()), name='BookingList'),
    path('search_house', views.search_house, name='search-house'),
    path('add_house', views.add_house, name='add-house'),
    path('bookinglistadmin', login_required(views.booking_list_admin), name='bookinglistadmin'),
    path('<int:year>/<str:month>', views.booking_list_admin, name='bookinglistadmin'),
]
