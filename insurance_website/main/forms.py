from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models


class LogInForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)

class UserRegistrationForm(UserCreationForm):

    address1 = forms.CharField(max_length=200)
    address2 = forms.CharField(max_length=200)
    state = forms.CharField(max_length=200)
    city = forms.CharField(max_length=200)
    zip = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2'
                  ]

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)

        # userInfo = models.UserInfo()
        # userInfo.address1 = self.cleaned_data['address1']
        # if(self.cleaned_data['address2']) != "":
        #     userInfo.address2 = self.cleaned_data['address2']
        # userInfo.city = self.cleaned_data['city']
        # userInfo.state = self.cleaned_data['state']
        # userInfo.zip = self.cleaned_data['zip']


