from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def admin(request):
    """ A view to return the index page """

    return render(request, 'home/admin.html')
