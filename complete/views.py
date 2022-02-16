from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import BookingForm
from services.models import Service
from .models import Booking, BookingLineItem
from django.core.mail import send_mail
from django.template.loader import render_to_string


def complete(request):
    """ Checks that a form is posted """
    # Checking if a form was posted
    if request.method == 'POST':
        book = request.session.get('book', [])
        if not book:
            messages.error(request, "There's no service pending to book")
            return redirect(reverse('services'))

        form = BookingForm(request.POST)

        if form.is_valid():
            form_data = {
                'full_name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email'],
                'phone_number': form.cleaned_data['phone_number'],
                'more_information': form.cleaned_data['more_information'],
            }

        completedForm = BookingForm(form_data)

        # Checking if the form is valid
        if completedForm.is_valid():
            service = Service.objects.get(id=book[0])
            booking = completedForm.save()
            del request.session['book']
            booking_line_item = BookingLineItem(
                booking=booking,
                service=service,
            )
            booking_line_item.save()

            # Return user to a successful page
        return redirect(reverse('booking_success',
                                args=[booking.booking_number]))

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

    if 'book' in request.session:
        del request.session['book']

    template = 'complete/booking_success.html'
    context = {
        'booking': booking,
    }

    cust_email = booking.email
    subject = render_to_string(
        'complete/confirmation_emails/confirmation_email_subject.txt',
        {'booking': booking})
    body = render_to_string(
        'complete/confirmation_emails/confirmation_email_body.txt',
        {'booking': booking, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )

    return render(request, template, context)
