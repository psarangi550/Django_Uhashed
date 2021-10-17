from django import forms #importing the forms module from django
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
class Register(UserCreationForm):
    class Meta:
        model=User
        fields = ("username","first_name","last_name","email","password1","password2")

class ProfileUserChange(UserChangeForm):
    model=User
    fields = ("username","first_name","last_name","email")
