from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# from django.conf import settings

from .forms import BookingForm
from services.models import Service
from .models import Booking, BookingLineItem
# from book.contexts import book_contents


def complete(request):
    """  """
    # Checking if a form was posted
    if request.method == 'POST':
        book = request.session.get('book', [])
        print(book)
        if not book:
            messages.error(request, "There's no service pending to book")
            return redirect(reverse('services'))

        # Assigning the posted data to a form variable
        form = BookingForm(request.POST)

        # you can assign all the values you recieved on the form to the data base Ive done one
        if form.is_valid():
            form_data = {
                'full_name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email'],
                'phone_number': form.cleaned_data['phone_number'],
                'more_information': form.cleaned_data['more_information'],
            }

        completedForm = BookingForm(form_data)
        print(completedForm['full_name'])
        print('form-data')

        # Checking if the form is valid
        if completedForm.is_valid():
            booking = completedForm.save()
            del request.session['book']

            # Return user to a successful page
            # return redirect(reverse('services'))
            return redirect(reverse('booking_success', args=[booking.booking_number]))
        # current_book = book_contents(request)

    else:

        booking_form = BookingForm()
        template = 'complete/complete.html'
        context = {
            'booking_form': booking_form,
        }

        return render(request, template, context)


def booking_success(request, booking_number):
    """ Handle Successful Bookings """
    booking = get_object_or_404(Booking, booking_number=booking_number)
    messages.success(request, f'Booking successfully processed! \
        Your booking number is {booking_number}. A confirmation \
        email will be sent to {booking.email}.')

    if 'book' in request.session:
        del request.session['book']

    template = 'complete/booking_success.html'
    context = {
        'booking': booking,
    }

    return render(request, template, context)
