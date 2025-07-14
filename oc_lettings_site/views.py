# 🌐 Imports
from django.shortcuts import render

# Internal Imports
from lettings.models import Letting
from profiles.models import Profile


# 🏠 Homepage View
def index(request):
    """Render the homepage with lists of profiles and lettings."""

    # 📋 Get all profiles and lettings
    profiles_list = Profile.objects.all()
    lettings_list = Letting.objects.all()

    # 🧩 Context passed to the template
    context = {
        'profiles_list': profiles_list,
        'lettings_list': lettings_list,
    }

    # 🖼️ Render the index.html template
    return render(request, 'index.html', context)


def custom_404(request, exception):
    """Custom 404 error page view."""
    return render(request, 'custom_404.html', status=404)


def custom_500(request):
    """Custom 500 error page view."""
    return render(request, 'custom_500.html', status=500)
