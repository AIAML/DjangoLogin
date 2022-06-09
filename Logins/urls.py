from django.urls import path
from .views import (
    LoginView
)

app_name = "Logins"
urlpatterns = [
    #path('login/', LoginView.as_view(), name="Logins-view"),
]

