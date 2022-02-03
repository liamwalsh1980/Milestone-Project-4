from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


# Decorator to wrap around the function to check user access before executing
@login_required
def admin(request):
    """ A view to return the index page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access this.')
        return redirect(reverse('home'))

    return render(request, 'home/admin.html')
