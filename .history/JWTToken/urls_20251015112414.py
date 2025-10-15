from django.urls import path
from .views import RegisterView, ProtectedView, LoginAPIView, mySwaggerGetView, HelloMessage, MySecureView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register-user"),
    path('protect/', ProtectedView.as_view(), name="protect-access"),
    path('login/', LoginAPIView.as_view(), name = "user-login"),
    path('hello/', HelloMessage.as_view(), name="hello"),
    path('swaggerPath/', mySwaggerGetView.as_view(), name='swagger'),
    path('secure/', MySecureView.as_view(), name="secure-api"),
]