from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

# Create your views here.


def base(request):
    return render(request, 'base.html', {})


def booking_list_admin(request, year, month):
    user = 'admin'
    month = month.capitalize()
    # converting month to numbers
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # print out a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    return render(request, 'booking_list_admin.html', {
        'user': user,
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal
    })
