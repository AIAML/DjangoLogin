from django.urls import path
from django.conf.urls import url
from .views import (
    LoginView,RegisterView
)

app_name = "Logins"
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
]
