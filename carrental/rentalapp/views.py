from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,AddVehicleForm
from django.contrib import messages
from .models import Person,Vehicle
# Create your views here.
@login_required(login_url='Login')
def home(request):
    print(request.user.username)
    print(Person.objects.filter(user=request.user))
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
            user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
            user.save()
            phone=request.POST['phone']
            age=request.POST['age']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            address=request.POST['address']
            profile_pic=request.POST['profile_pic']
            print(first_name)
            new_person=Person(user=user,first_name=first_name,last_name=last_name,email=email,phone=phone,address=address,age=age,profile_pic=profile_pic)
            new_person.save()
            login(request, user)
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

@login_required(login_url='Login')
def book_vehicle(request):
    return render(request,'book_vehicle.html')

@login_required(login_url='Login')
def add_vehicle(request):
    if request.method == 'POST':
        form=AddVehicleForm(request.POST)
        if form.is_valid():
            print(request.user)
            vehicle=Vehicle(
                brand_name=request.POST['brand_name'],
                model_name=request.POST['model_name'],
                registration_number=request.POST['registration_number'],
                year=request.POST['year'],
                description=request.POST['description'],
                category=request.POST['category'],
                km_driven=request.POST['km_driven'],
                pic=request.POST['pic'],
                owner=Person.objects.filter(user=request.user)[0]
            )
            vehicle.save()
            context={'form':form}
            print(request.POST)
            return redirect('Home')
    form=AddVehicleForm()
    return render(request,'add_vehicle.html',{'form':form})
