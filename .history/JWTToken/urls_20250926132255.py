from django.urls import path
from .views import RegisterView, ProtectedView

urlpatterna = [
    path('register/', RegisterView),
    path('protect/', ProtectedView)
]