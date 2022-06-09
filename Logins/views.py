from django.shortcuts import render, get_object_or_404,Http404
from django.views import View
from .forms import *
from .models import Loginmodels


class LoginView(View):
    template_name = "Login_page.html"

    def get(self, request, *args, **kwargs):
        # GET Method
        #obj = get_object_or_404(Loginmodels)
        form = LoginModelForm()
        context = {}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST Method
        form = LoginModelForm(request.POST)
        if form.is_valid():
            obj = get_object_or_404(Loginmodels,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            print(obj.username)

        # form.save()
        context = {}
        return render(request, self.template_name, context)
