from django.urls import path
from . import views


app_name = "lettings"

urlpatterns = [
    path('index/', views.lettings_index, name='index'),
    path('<int:letting_id>/', views.get_letting, name='letting')
]
