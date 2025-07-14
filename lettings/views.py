# 🌐 Imports
from django.shortcuts import render
from .models import Letting


# 📄 Lettings Index View
def lettings_index(request):
    """Display a list of all lettings."""

    # 📋 Get all lettings
    lettings_list = Letting.objects.all()

    # 🧩 Context for the template
    context = {'lettings_list': lettings_list}

    # 🖼️ Render lettings index template
    return render(request, 'lettings/index.html', context)


# 🔍 Letting Detail View
def get_letting(request, letting_id):
    """Display the details of a specific letting by ID."""

    # 🎯 Get letting by ID
    letting = Letting.objects.get(id=letting_id)

    # 🧩 Context for the template
    context = {
        'title': letting.title,
        'address': letting.address,
    }

    # 🖼️ Render letting details template
    return render(request, 'lettings/letting_details.html', context)
