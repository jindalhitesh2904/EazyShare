from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Person

class CreateUserForm(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=250)
    phone=PhoneNumberField()
    address=forms.CharField(max_length=250)
    age=forms.IntegerField()
    class Meta:
        model=User
        fields=[
            'username','first_name','last_name','email','phone','address','age','password1','password2',
        ]