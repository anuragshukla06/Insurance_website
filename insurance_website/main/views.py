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
    return render(request, 'index.html', {"loggedIn": request.user.is_authenticated, "userName": request.user.username, "name": userName})

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
        return render(request, 'register.html', {"loggedIn": request.user.is_authenticated})


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
def showPlan(request, planNo):

    if request.method == "POST":
        form = forms.InsuranceRegForm(request.POST or None)
        if form.is_valid():
            insuranceReg = models.Insurance()
            insuranceReg.user = request.user
            insuranceReg.Active = False
            insuranceReg.Request = True
            planNo = form.cleaned_data["planNo"]
            insuranceReg.Plan = planNo
            insuranceReg.save()
            return render(request, "showInsuranceDetail.html", {"buyRequest": 1, "planNo": planNo})
        else:
            return HttpResponse("ERROR, SOMETHING WENT WRONG!")

    return render(request, "showInsuranceDetail.html", {"planNo": planNo,
                                                        "loggedIn": loggedIn,
                                                        "details": {"price": 500,
                                                                    "duration": 3,
                                                                    "benifit": 1200000},
                                                        "userActive": request.user.is_authenticated,
                                                        "buyRequest": 0,

                                                        })
def profile(request, username):
    allInsurance = models.Insurance.objects.filter(user = request.user)
    allClaims = []
    for insurance in allInsurance:
        claim = models.Claims.objects.filter(Insurance_claimed = insurance)
        if len(claim) != 0:
            allClaims.append(claim[0])
    userInfo = models.UserInfo.objects.get(user=request.user)
    return render(request, "profile.html", {"username": username,
                                            "allInsurance": allInsurance,
                                            "allClaims": allClaims,
                                            "userInfo": userInfo,
                                            "user": user})

def claimInsurance(request):
    if request.method == "POST":
        form = forms.ClaimInsuranceForm(request.POST or None)

        if form.is_valid():
            insuranceId = form.cleaned_data["insuranceId"]
            insuranceObject = models.Insurance.objects.get(id=insuranceId)
            if insuranceObject.Claimed == False:
                claimObject = models.Claims()
                insuranceObject.Claimed = True
                claimObject.Insurance_claimed = insuranceObject
                claimObject.Handled = False
                claimObject.save()
                insuranceObject.save()
                return redirect(profile, request.user.username)
            else:
                return HttpResponse("Already Claimed")
    else:
        return HttpResponse("Error why")

def paymentConfirmation(request, planNo):

    return  render(request, "paymentConfirmation.html", {"planNo": planNo})
# def resource(request):
#     return render(request, 'resource.html', {})