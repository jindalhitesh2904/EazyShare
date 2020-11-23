from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Person,Vehicle

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

class AddVehicleForm(forms.Form):
    class Meta:
        model=Vehicle
        exclude=['owner']
        # fields=['brand_name','model_name','registration_number','year','description','category','km_driven','pic',]

class EditProfileForm(forms.ModelForm):
    class Meta:
        model=Person
        exclude=['owner']