from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from Logins.views import LoginView, RegisterView,MainPageView,LoginoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Logins/', include('Logins.urls')),
    path('', LoginView.as_view(), name='home'),
    url(r'^$', LoginView.as_view(), name='home'),
    url(r'^register/$', RegisterView.as_view(), name='register-link'),
    url(r'^Logout/$', LoginoutView.as_view(), name='Logout'),
    path('mainpage/', MainPageView.as_view(), name="main"),
    path('login/', LoginView.as_view(), name="home"),
    path('logout/', LoginoutView.as_view(), name="Logout"),

]
