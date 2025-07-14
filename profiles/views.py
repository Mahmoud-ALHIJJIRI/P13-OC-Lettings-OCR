from django.shortcuts import render
from .models import Profile


def profiles_index(request):
    """
    Display a list of all user profiles.
    """
    profiles_list = Profile.objects.all()  # Retrieve all profile objects
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def get_profile(request, username):
    """
    Display the profile of a specific user by username.
    """
    profile = Profile.objects.get(user__username=username)  # Fetch profile by username
    context = {'profile': profile}
    return render(request, 'profiles/profile_details.html', context)
