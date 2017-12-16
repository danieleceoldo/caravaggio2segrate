from django.contrib import admin

# Register your models here.

from .models import CustomerData, BookingReference, BookingCalendar

class CustomerDataAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'address', 'city', 'nationality',
            'phone', 'email')
    list_filter = ['surname', 'name', 'email']
    search_fields = ['surname', 'name', 'email']

admin.site.register(CustomerData, CustomerDataAdmin)

class BookingReferenceAdmin(admin.ModelAdmin):
    list_display = ('creationdate', 'lastmodifieddate', 'adultsnum',
            'kidsnum', 'customerdata')

admin.site.register(BookingReference, BookingReferenceAdmin)

class BookingCalendarAdmin(admin.ModelAdmin):
    list_display = ('bookingdate', 'bookingstate', 'bookingreference')
    list_filter = ('bookingdate', 'bookingstate', 'bookingreference')
    search_fields = ['bookingdate', 'bookingstate', 'bookingreference__creationdate']

admin.site.register(BookingCalendar, BookingCalendarAdmin)
