from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# Used to handle complex query in the database to achieve 'or' logic
# To match either from product name or product description - use Q
from django.db.models import Q
from .models import Service, ServiceCategory

# Create your views here.


def all_services(request):
    """ A view to show all services, including sorting and search queries """

    services = Service.objects.all()
    query = None
    servicescategories = None

    if request.GET:
        if 'servicecategory' in request.GET:
            servicescategories = request.GET['servicecategory'].split(',')
            services = services.filter(image__name__in=servicescategories)
            servicescategories = ServiceCategory.objects.filter(name__in=servicescategories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('services'))

            # Pipe gives the 'or' statement
            # 'i' makes both name and description case insensitive
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            services = services.filter(queries)

    context = {
        'services': services,
        'search_term': query,
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
