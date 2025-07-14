from django.shortcuts import render
from .models import Letting


def lettings_index(request):
    """
    Display a list of all lettings.
    """
    lettings_list = Letting.objects.all()  # Retrieve all letting objects
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def get_letting(request, letting_id):
    """
    Display the details of a specific letting by ID.
    """
    letting = Letting.objects.get(id=letting_id)  # Fetch letting by its ID
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting_details.html', context)
