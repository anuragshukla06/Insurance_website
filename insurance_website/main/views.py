from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import forms
from . import models

# Create your views here.
user = None
loggedIn = 0
def home(request):
    userName = ""
    if user is not None:
        userName = user.first_name
    return render(request, 'index.html', {"loggedIn": loggedIn, "userName": userName})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def insurance(request):
    return render(request, 'insurance.html', {})

def register(request):
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST or None)
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

        return render(request, 'register.html', {"loggedIn": loggedIn})


def login_view(request):
    if request.method == "POST":
        form = forms.LogInForm(request.POST or None)
        if form.is_valid():
            global user, loggedIn
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user == None:
                return HttpResponse("Not able to login")
            else:
                login(request, user)
                loggedIn = 1
                return redirect(home)

    else:
        return render(request, "login.html", {})
def logout_view(request):
    logout(request)
    global loggedIn, user
    loggedIn = 0
    user = None
    return redirect(home)
# def resource(request):
#     return render(request, 'resource.html', {})