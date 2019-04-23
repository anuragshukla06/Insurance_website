from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import forms
from . import models

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def insurance(request):
    return render(request, 'insurance.html', {})

def register(request):
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST or None)
        form.save()
        if form.is_valid():
            form.save()

            userInfo = models.UserInfo()
            userInfo.address1 = form.cleaned_data['address1']
            if (form.cleaned_data['address2']) != "":
                userInfo.address2 = form.cleaned_data['address2']
            userInfo.city = form.cleaned_data['city']
            userInfo.state = form.cleaned_data['state']
            userInfo.zip = form.cleaned_data['zip']
            userInfo.user = User.objects.get(username=form.cleaned_data["username"])
            userInfo.save()

            return redirect(register)
        else:
            return HttpResponse("Something went wrong!")

    else:

        return render(request, 'register.html', {})

# def resource(request):
#     return render(request, 'resource.html', {})