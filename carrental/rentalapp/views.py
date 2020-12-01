from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,AddVehicleForm,EditProfileForm,CreateBookingForm
from django.contrib import messages
from .models import Person,Vehicle, Bookings
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from datetime import date
# Create your views here.
@login_required(login_url='Login')
def home(request):
    # bookings = Bookings.objects.all()
    bookings = Bookings.objects.filter(status__exact='AVAILABLE').exclude(vehicle__owner__user=request.user)  
    return render(request,'home.html', {'bookings':bookings})

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
    return redirect('Home')

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
                brand_name=request.POST.get('brand_name', 'XXXXX'),
                model_name=request.POST.get('model_name'),
                registration_number=request.POST.get('registration_number'),
                year=request.POST.get('year', '2020'),
                description=request.POST.get('description', 'This is a good vehicle'),
                category=request.POST.get('category', 'Car'),
                km_driven=request.POST.get('km_driven', '1000'),
                pic=request.POST.get('pic'),
                owner=Person.objects.filter(user=request.user)[0]
            )
            vehicle.save()
            context={'form':form}
            print(request.POST)
            return redirect('Home')
    form=AddVehicleForm()
    return render(request,'add_vehicle.html',{'form':form})

class ListMyVehicles(generic.ListView):
    template_name='list_my_vehicles.html'
    context_object_name='vehicles_list'

    def get_queryset(self):
        return Vehicle.objects.filter(owner__user=self.request.user)

class EditProfile(generic.UpdateView):
    model=Person
    template_name='edit_profile.html'
    fields=['first_name','last_name','profile_pic','email','phone','address','age']
    success_url=reverse_lazy('Home')

    def get_object(self):
        return Person.objects.filter(user=self.request.user)[0]

# class EditVehicle(generic.UpdateView):
#     model=Person
#     template_name='edit_vehicle.html'
#     fields=['brand_name','model_name','registration_number','year','description','category','km_drive','pic']
#     success_url=reverse_lazy('Home')

@login_required(login_url='Login')
def CreateBooking(request,vehicle_id):
    if request.method=="POST":
        form=CreateBookingForm(request.POST)
        if form.is_valid():
            booking=Bookings(
                status='AVAILABLE',
                start_date=request.POST['start_date'],
                end_date=request.POST['end_date'],
                per_km_cost=request.POST['per_km_cost'],
                per_day_cost=request.POST['per_day_cost'],
                cost='0',
                lender=Person.objects.filter(user=request.user)[0],
                vehicle=Vehicle.objects.get(id=vehicle_id),
            )
            booking.save()
            return redirect('Home')
    form=CreateBookingForm()
    return render(request,'bookings_form.html',{'form':form})

@login_required(login_url='Login')
def BookBooking(request,booking_id):
    booking=Bookings.objects.get(id=booking_id)
    booking.status='BOOKED'
    booking.borrower=Person.objects.filter(user=request.user)[0]
    booking.save()
    messages.success(request,'Booking done')
    return redirect('Home')

@login_required(login_url='Login')
def MyBorrowings(request):
    borrowings=Bookings.objects.filter(status__exact='BOOKED',borrower=Person.objects.filter(user=request.user)[0])
    return render(request,'my_borrowings.html',{'borrowings':borrowings})

@login_required(login_url='Login')
def EndBooking(request,borrowing_id):
    if request.method=="POST":
        borrowing=Bookings.objects.get(id=borrowing_id)
        borrowing.status='COMPLETED'
        days=borrowing.end_date-borrowing.start_date+1
        borrowing.km_drove=request.POST['km_drove']
        borrowing.cost=max(km_drove*borrowing.cost_per_km,days*borrowing.cost_per_day)
        borrowing.save()
        # alert("pay"+borrowing.borrower+borrowing.cost+"rupees")
        print(borrowing.cost)
        return redirect('my_borrowings')
    return redirect('Home')

@login_required(login_url='Login')
def ViewProfile(request,username):
    profile=Person.objects.get(user__username=username)
    return render(request,'view_profile.html',{'profile':profile})

@login_required(login_url='Login')
def MyLendings(request):
    lendings=Bookings.objects.filter(lender=Person.objects.filter(user=request.user)[0])
    return render(request,'my_lendings.html',{'lendings':lendings})