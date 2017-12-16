from django.shortcuts import render
import datetime

from .models import BookingCalendar

# Create your views here.

def index(request):
    return render(request, 'index/index.html')

def checkavail(request):
    checkinstr = request.POST['CheckIn']
    checkoutstr = request.POST['CheckOut']
    adultsstr = request.POST['Adults']
    kidsstr = request.POST['Kids']

    checkindate = datetime.date(int(checkinstr[4:8]), int(checkinstr[2:4]),
            int(checkinstr[:2]))
    checkoutdate = datetime.date(int(checkoutstr[4:8]), int(checkoutstr[2:4]),
            int(checkoutstr[:2]))

    daysnum = (checkoutdate - checkindate).days

    availability = {}
    booknow = True
    for day in range(daysnum):
        checkdate = checkindate + datetime.timedelta(day)
        filtdate = BookingCalendar.objects.filter(bookingdate=checkdate)
        if len(filtdate) == 0:
            checkresult = 'Available'
        else:
            checkresult = 'Not Available'
            booknow = False
        availability.update({checkdate.strftime('%d-%m-%Y'): checkresult})

    return render(request, 'index/checkavail.html', {
        'checkinstr': checkinstr,
        'checkoutstr': checkoutstr,
        'adultsstr': adultsstr,
        'kidsstr': kidsstr,
        'checkindate': checkindate.strftime('%d-%m-%Y'),
        'checkoutdate': checkoutdate.strftime('%d-%m-%Y'),
        'availability_list': sorted(availability.items()),
        'booknow': booknow,
        })
