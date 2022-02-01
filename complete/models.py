import uuid

from django.db import models

from services.models import Service


class Booking(models.Model):
    booking_number = models.CharField(max_length=32, null=False,
                                      editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    more_information = models.TextField(null=True, blank=True, default='')
    date = models.DateTimeField(auto_now_add=True)

    def _generate_booking_number(self):
        """
        Generate a random, unique booking number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the booking number
        if it hasn't been set already.
        """
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_number


class BookingLineItem(models.Model):
    booking = models.ForeignKey(Booking, null=False, blank=False,
                                on_delete=models.CASCADE,
                                related_name='lineitems')
    service = models.ForeignKey(Service, null=False, blank=False,
                                on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """
        Override the original save method
        """
        self.service
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Booking number:{self.booking.booking_number}'
