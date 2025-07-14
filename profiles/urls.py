from django.urls import path
from . import views


app_name = "profiles"

urlpatterns = [
    path('index/', views.profiles_index, name='index'),
    path('profiles/<str:username>/', views.get_profile, name='profile'),
]
