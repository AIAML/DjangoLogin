from django.shortcuts import render, get_object_or_404,Http404
from django.views import View
from .forms import *
from .models import Loginmodels


class LoginView(View):
    template_name = "Login_page.html"
    def get(self, request, *args, **kwargs):
        # GET Method
        context = {}
        context['state'] = 'firsttime'
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST Method
        form = LoginModelForm(request.POST)
        if form.is_valid():
            context = {}
            try:
                obj = get_object_or_404(Loginmodels,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
                print(obj.username)
                context['state'] = 'success'
            except:
                obj = None
                context['state'] = 'failed'

        return render(request, self.template_name, context)

class RegisterView(View):
    template_name = "Register_page.html"
    def get(self, request, *args, **kwargs):
        # GET Method
        context = {}
        context['state'] = 'firsttime'
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST Method
        form = LoginModelForm(request.POST)
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
                    obj = get_object_or_404(Loginmodels,username=form.cleaned_data['username'])
                    context['state'] = '4'
                except:
                    obj = None
                    form.save()
                    context['state'] = '5'
        else:
            context['state'] = '-1'
        return render(request, self.template_name, context)

