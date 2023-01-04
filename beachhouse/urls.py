from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import BookingList, AddBooking

urlpatterns = [
    path('', views.base, name='base'),
    path('index', views.index, name='index'),
    path('houselist', views.house_list, name='houselist'),
    path('add_booking/<house_id>', login_required(AddBooking.as_view()), name='add_booking'),
    path('bookings_list', login_required(BookingList.as_view()), name='BookingList'),
    path('bookinglistadmin', login_required(views.booking_list_admin), name='bookinglistadmin'),
    path('<int:year>/<str:month>', views.booking_list_admin, name='bookinglistadmin'),
]
