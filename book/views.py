from django.shortcuts import render, redirect, get_object_or_404
from services.models import Service


# Create your views here.


def service_booking(request):
    """ A view that renders the booking page """

    book = request.session.get('book', [])

    service = get_object_or_404(Service, id=book[0])
    print(service)

    context = {"book_service": service}

    return render(request, 'book/service_booking.html', context)


def add_to_booking(request, item_id):
    """ Add a booking """

    service = get_object_or_404(Service, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    book = request.session.get('book', [])
    
    # print('Book =', book)
    request.session['book'] = [service.id]
    print(service.id)

    return redirect(redirect_url)
