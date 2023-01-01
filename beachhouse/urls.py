from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('index', views.index, name='index'),
    path('houselist', views.house_list, name='houselist'),
    path('add_booking', views.add_booking, name='add-booking'),
    path('bookinglistadmin', views.booking_list_admin, name='bookinglistadmin'),
    path('<int:year>/<str:month>', views.booking_list_admin, name='bookinglistadmin'),
]
