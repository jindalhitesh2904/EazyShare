from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.
@login_required(login_url='Login')
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('Home')
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request,'Account created successfully!')
            login(request,user)
            context={'form':form}
            return redirect('Home')
    context={'form':form}
    return render(request,'sign_up.html',context)

def signin(request):
    if request.user.is_authenticated:
        return redirect('Home')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'logged in successfully!')
            return redirect('Home')
        else:
            messages.info(request,'username or password is incorrect')
    context={}
    return render(request,'login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('Login')