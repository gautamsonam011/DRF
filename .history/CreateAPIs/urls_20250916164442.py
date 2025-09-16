from django.urls import path
from .views import create_views_data, get_all_data, update_record


urlpatterns = [
    path('post/', create_views_data),
    path('getAll/', get_all_data), 
    path('update/<int:pk>/', update_record),
]