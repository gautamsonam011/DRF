from django.urls import path
from .views import create_views_data, get_all_data


urlpatterns = [
    path('post/', create_views_data),
    path('getAll/', get_all_data)
]