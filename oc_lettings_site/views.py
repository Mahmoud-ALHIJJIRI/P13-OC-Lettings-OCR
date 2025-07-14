from django.shortcuts import render
from lettings.models import Letting
from profiles.models import Profile


def index(request):
    """
    Render the main index page of the website.
    """
    profiles_list = Profile.objects.all()
    lettings_list = Letting.objects.all()
    context = {
        'profiles_list': profiles_list,
        'lettings_list': lettings_list
    }
    return render(request, 'index.html', context)
