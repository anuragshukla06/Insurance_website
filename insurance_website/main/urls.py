from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<username>', views.profile,  name="profile"),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('insurance', views.insurance, name='insurance'),
    path('register', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('planDetails/<int:planNo>', views.showPlan, name="showPlan"),
    path('paymentConfirmation/<int:planNo>', views.paymentConfirmation, name="paymentConfirmation"),
    path('claim', views.claimInsurance, name="claim")
    # path('resource', views.resource, name='resource')
]