from django.urls import path
from django.conf.urls import url
from .views import (
    LoginView,RegisterView,MainPageView
)
from . import views

app_name = "Logins"
urlpatterns = [
    path('login/', LoginView.as_view(), name="register"),
    path('register/', RegisterView.as_view(), name="register"),
    path('mainpage/', MainPageView.as_view(), name="main"),
    path('members/',views.members, name="members"),
    path('members/details/<int:id>',views.details, name="members_details"),
]
