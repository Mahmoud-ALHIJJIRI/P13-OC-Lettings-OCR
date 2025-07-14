"""
🌐 URL configuration for the profile's app.
Handles routing for the profiles index and individual profile views.
"""

from django.urls import path
# 📦 Internal imports
from . import views

# 🔖 App namespace
app_name = "profiles"

# 🧭 URL patterns
urlpatterns = [
    path('index/', views.profiles_index, name='index'),  # 📄 Profiles list view
    path('<str:username>/', views.get_profile, name='profile'),  # 🔍 Profile detail view
]
