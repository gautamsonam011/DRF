from django.urls import path
from .views import create_views_data


urlpatterns = [
    path('post/', create_views_data),
]