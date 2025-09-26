from django.urls import path
from .views import RegisterView, ProtectedView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register-user"),
    path('protect/', ProtectedView.as_view(), name="protect-access"),
]