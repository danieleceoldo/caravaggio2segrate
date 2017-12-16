from django.db import models

# Create your models here.


class CustomerData(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.surname

class BookingReference(models.Model):
    creationdate = models.DateTimeField(auto_now_add=True)
    lastmodifieddate = models.DateTimeField(auto_now=True)
    adultsnum = models.DecimalField(max_digits=1, decimal_places=0)
    kidsnum = models.DecimalField(max_digits=1, decimal_places=0)
    customerdata = models.ForeignKey(CustomerData, on_delete=models.CASCADE)

    def __str__(self):
        return self.creationdate.__str__()

class BookingCalendar(models.Model):
    ToBeConfirmed = 'TBC'
    Confirmed = 'CON'
    NotAvailable = 'N/A'
    BookingState = (
            (ToBeConfirmed, 'TO BE CONFIRMED'),
            (Confirmed, 'CONFIRMED'),
            (NotAvailable, 'NOT AVAILABLE'),
            )
    bookingdate = models.DateField(unique=True)
    bookingstate = models.CharField(max_length=3, choices=BookingState,
            default=ToBeConfirmed)
    bookingreference = models.ForeignKey(BookingReference, on_delete=models.CASCADE)

    def __str__(self):
        return self.bookingdate.__str__()
