# 🌐 Imports
from django.shortcuts import render
from .models import Profile


# 📄 Profiles Index View
def profiles_index(request):
    """Display a list of all user profiles."""

    # 📋 Get all profiles
    profiles_list = Profile.objects.all()

    # 🧩 Context for the template
    context = {'profiles_list': profiles_list}

    # 🖼️ Render profiles index template
    return render(request, 'profiles/index.html', context)


# 🔍 Profile Detail View
def get_profile(request, username):
    """Display the profile of a specific user by username."""

    # 🎯 Get profile by username
    profile = Profile.objects.get(user__username=username)

    # 🧩 Context for the template
    context = {'profile': profile}

    # 🖼️ Render profile details template
    return render(request, 'profiles/profile_details.html', context)
