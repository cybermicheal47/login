from django.contrib.auth.forms import  UserChangeForm
from django import forms
from django.contrib.auth.models import User

class editprofile(UserChangeForm):
    class Meta :
        model = User
        fields = (
            
        )
