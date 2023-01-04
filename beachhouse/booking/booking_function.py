import datetime
from beachhouse.models import House, Bookings


def check_availability(house, checkin, checkout):
    avail_list = []
    booking_list = Bookings.objects.filter(house=house)
    for booking in booking_list:
        if booking.checkin > checkout or booking.checkout < checkin:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
