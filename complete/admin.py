from django.contrib import admin
from .models import Booking, BookingLineItem


class BookingLineItemAdminInline(admin.TabularInline):
    model = BookingLineItem


class BookingAdmin(admin.ModelAdmin):
    inlines = (BookingLineItemAdminInline,)

    readonly_fields = ('booking_number', 'date',)

    fields = ('booking_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'more_information',)

    list_display = ('booking_number', 'date', 'full_name',)

    ordering = ('-date',)


admin.site.register(Booking, BookingAdmin)
