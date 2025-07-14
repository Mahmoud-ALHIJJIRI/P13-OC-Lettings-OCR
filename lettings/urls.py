"""
🌐 URL configuration for the letting's app.
Handles routing for the lettings index and detail pages.
"""

from django.urls import path
from . import views

# 🔖 App namespace
app_name = "lettings"

# 🧭 URL patterns
urlpatterns = [
    path('index/', views.lettings_index, name='index'),       # 📄 Lettings list view
    path('<int:letting_id>/', views.get_letting, name='letting'),  # 🔍 Letting detail view
]
