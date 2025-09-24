from django.urls import path
from .views import create_views_data, get_all_data, update_record, vehicle_details_op, SendOTPView, VerifyOTPView, ProfileAPI


urlpatterns = [
    path('post/', create_views_data),
    path('getAll/', get_all_data), 
    path('update/<int:pk>/', update_record),
    path('vehicle/<int:pk>/', vehicle_details_op),
    path('send_otp/', SendOTPView.as_view(), name = 'send-otp'),
    path('verify_otp/', VerifyOTPView.as_view(), name = 'verify-otp'),
    path('profile/', ProfileAPI.as_view(), name = 'profile'),
]