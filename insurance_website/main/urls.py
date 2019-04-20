from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('insurance', views.insurance, name='insurance'),
    path('register', views.register, name='register'),
    # path('resource', views.resource, name='resource')
]