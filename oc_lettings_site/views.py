# 🌐 Imports
from django.shortcuts import render
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
