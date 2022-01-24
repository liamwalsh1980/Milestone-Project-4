from django.shortcuts import get_object_or_404
from services.models import Service


def book_contents(request):

    book_service = []
    name = []
    number = []
    email = []
    infobox = []
    book = request.session.get('book', {})

    for item_id, service in book.items():
        service = get_object_or_404(Service, pk=item_id)
        book_service.append({
            'item_id': item_id,
            'service': service,
        })

    context = {
        'book_service': book_service,
        'name': name,
        'number': number,
        'email': email,
        'infobox': infobox,
    }

    return context
