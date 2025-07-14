"""
🌐 Root URL configuration for the Django project.
Includes routes for admin, index, lettings, and profiles apps.
"""
from django.contrib import admin
from django.urls import path, include
# 📦 Internal imports
from . import views

# 🧭 Main URL patterns
urlpatterns = [
    path("", views.index, name="index"),  # 🏠 Homepage
    path("admin/", admin.site.urls),  # ⚙️ Django admin
    path("lettings/", include(("lettings.urls", "lettings"), namespace="lettings")),  # 🏘️ Lettings app
    path("profiles/", include(("profiles.urls", "profiles"), namespace="profiles")),  # 👤 Profiles app
]
