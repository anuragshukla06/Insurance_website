from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'register.html', {})

# def resource(request):
#     return render(request, 'resource.html', {})