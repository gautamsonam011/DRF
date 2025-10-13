from django.urls import path
    
    
from .views import create_views_data, get_all_data, update_record, call_vehicle, vehicle_list_view, vehicle_details_op, postProfile, CallVehicleNamesView, SendOTPView, VerifyOTPView, ItemList, google_map_view, my_google_map_view, weather_api_view


urlpatterns = [
    path('post/', create_views_data),
    path('getAll/', get_all_data), 
    path('update/<int:pk>/', update_record),
    path('vehicle/<int:pk>/', vehicle_details_op),
    path('send_otp/', SendOTPView.as_view(), name = 'send-otp'),
    path('verify_otp/', VerifyOTPView.as_view(), name = 'verify-otp'),
    # path('profile/', ProfileAPI.as_view(), name = 'profile'),
    path('profile/', postProfile),
    path('map/', google_map_view),
    path('googlemap/', my_google_map_view), 
    path('weather/', weather_api_view),
    path('item/', ItemList.as_view(), name = "item"),
    path('<str:version>/items/', ItemList.as_view(), name='items'),
    path('vehicleNames/', CallVehicleNamesView.as_view(), name="vehicle-name"),
    path('vehicle-names/', call_vehicle),
    path('cache/', vehicle_list_view),
    
    ]
