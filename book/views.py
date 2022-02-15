from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from services.models import Service


def service_booking(request):
    """ A view that renders the booking page """

    book = request.session.get('book', [])
    service = None
    if book:
        service = get_object_or_404(Service, id=book[0])

    context = {"book_service": service}

    return render(request, 'book/service_booking.html', context)


def add_to_booking(request, item_id):
    """ Add a booking """

    service = get_object_or_404(Service, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    request.session['book'] = [service.id]
    messages.success(request, f'"{service}" added')

    return redirect(redirect_url)


def remove_from_booking(request, item_id):
    """Remove the service from the booking"""

    try:
        service = get_object_or_404(Service, pk=item_id)

        book = request.session.get('book', {})

        book.pop(item_id)
        messages.success(request, f'{service} removed')

        request.session['book'] = book
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing service: {e}')
        return HttpResponse(status=500)
