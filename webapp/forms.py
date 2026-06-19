from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth. forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Record

from django import forms

# Register/Create a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# login form

class LoginForm(AuthenticationForm):
    username= forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# create a Record 

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name','email', 'phone', 'address', 'city', 'country', 'province']
    
# Update a Record 

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name','email', 'phone', 'address', 'city', 'country', 'province']