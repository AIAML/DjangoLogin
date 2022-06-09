from django.urls import path
from .views import (
    LoginView,RegisterView
)

app_name = "Logins"
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
]

