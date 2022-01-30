from django.shortcuts import render, get_object_or_404
from .models import Service


def all_services(request):
    """ A view to show all services, including sorting and search queries """

    services = Service.objects.all()
    servicescategories = None

    context = {
        'services': services,
        'current_servicecategories': servicescategories,
    }

    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    """ A view to show individual service details """

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_detail.html', context)
