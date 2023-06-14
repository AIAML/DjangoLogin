from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from .forms import *
from .models import Loginmodels
from http import cookies
from django.template import loader
import datetime

def members(request):
    template_name = "members.html"
    context = {}

    template = loader.get_template(template_name)
    # return HttpResponse(template.render())
    return render(request, template_name, context)







class LoginoutView(View):
    template_name = "Login_page.html"

    def get(self, request, *args, **kwargs):
        response = redirect('/login/')
        set_cookie(response, 'login_stamp', 'valid', -1)
        return response


class LoginView(View):
    template_name = "Login_page.html"

    def get(self, request, *args, **kwargs):
        context = {}
        try:
            print(request.COOKIES.get('login_stamp'))
            if request.COOKIES.get('login_stamp') == "valid":
                response = redirect('/mainpage/')
                set_cookie(response, 'login_stamp', 'valid')
                return response
            else:
                return render(request, self.template_name, context)
        except:
            obj = None
            return render(request, self.template_name, context)

        # GET Method
        context['state'] = 'firsttime'
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST Method
        form = LoginModelForm(request.POST)
        context = {}
        if form.is_valid():
            try:
                obj = get_object_or_404(Loginmodels, username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password'])
                print(obj.username)
                context['state'] = 'success'
                # response = HttpResponse('blah')
                # response.setcookie('login_stamp', 'valid')
                response = redirect('/mainpage/')
                set_cookie(response, 'login_stamp', 'valid')
                return response
            except:
                obj = None
                context['state'] = 'failed'

        return render(request, self.template_name, context)


class MainPageView(View):
    template_name = "Main_page.html"

    def get(self, request, *args, **kwargs):
        # GET Method
        try:
            print("test")
            print(request.COOKIES.get('login_stamp'))
            if request.COOKIES.get('login_stamp') == "valid":
                context = {}
                context['state'] = 'firsttime'
                return render(request, self.template_name, context)
            else:
                return redirect('/login/')
        except:
            obj = None
            return redirect('/login/')


class RegisterView(View):
    template_name = "Register_page.html"

    def get(self, request, *args, **kwargs):
        # GET Method
        context = {}
        context['state'] = 'firsttime'
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST Method
        form = RegisterModelForm(request.POST)
        context = {}
        if form.is_valid():
            if request.POST['repassword'] != form.cleaned_data['password']:
                context['state'] = '1'
            elif len(form.cleaned_data['password']) < 3:
                context['state'] = '2'
            elif len(form.cleaned_data['username']) < 3:
                context['state'] = '3'
            else:
                try:
                    obj = get_object_or_404(Loginmodels, username=form.cleaned_data['username'])
                    context['state'] = '4'
                except:
                    obj = None
                    form.save()
                    context['state'] = '5'
        else:
            context['state'] = '-1'
        return render(request, self.template_name, context)


def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
    )


def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('java-tutorial', 'javatpoint.com')
    return response


def getcookie(request):
    tutorial = request.COOKIES['java-tutorial']
    return HttpResponse("java tutorials @: " + tutorial);
