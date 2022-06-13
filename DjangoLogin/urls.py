from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from Logins.views import LoginView, RegisterView,MainPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Logins/', include('Logins.urls')),
    path('', LoginView.as_view(), name='home'),
    url(r'^$', LoginView.as_view(), name='home'),
    url(r'^register/$', RegisterView.as_view(), name='register-link'),
    path('mainpage/', MainPageView.as_view(), name="main"),
]
