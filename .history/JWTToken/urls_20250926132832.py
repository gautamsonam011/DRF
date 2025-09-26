from django.urls import path
from .views import RegisterView, ProtectedView

urlpatterns = [
    path('register/', RegisterView),
    path('protect/', ProtectedView)
]