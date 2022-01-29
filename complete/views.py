from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import BookingForm


def complete(request):
    book = request.session.get('book', [])
    if not book:
        messages.error(request, "There's no service pending to book at the moment")
        return redirect(reverse('services'))

    booking_form = BookingForm()
    template = 'complete/complete.html'
    context = {
        'booking_form': booking_form,
    }

    return render(request, template, context)
