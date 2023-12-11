from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Trains,Ticket

class Registeration(UserCreationForm):
    class Meta:
     model=User
     fields=['first_name','last_name','email','password1','password2']

class Train_form(forms.ModelForm):
    class Meta:
        model=Trains
        fields=['train_number','train_destination','date']

class User_form(forms.ModelForm):
    class Meta:
        model=Ticket
        fields='__all__'