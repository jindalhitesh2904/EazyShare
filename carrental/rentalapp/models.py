from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Lender(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	email=models.EmailField(max_length=250)
	phone=PhoneNumberField()
	address=models.CharField(max_length=250)
	age=models.IntegerField()
class Borrower(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	email=models.EmailField(max_length=250)
	phone=PhoneNumberField()
	address=models.CharField(max_length=250)
	age=models.IntegerField()
	
class Vehicle(models.Model):
	brand_name=models.CharField(max_length=100)
	year=models.IntegerField()
	description=models.TextField()
	km_driven=models.PositiveIntegerField()
	per_km_cost=models.PositiveIntegerField(default=12)
	per_day_cost=models.PositiveIntegerField(default=500)
	availability_start_date=models.DateField()
	availability_end_date=models.DateField(null=True)
	owner=models.ForeignKey(Lender,on_delete=models.CASCADE)
	category=models.CharField(max_length=20,choices=[('CAR','Car'),('SCOOTY','Scooty'),('MOTORBIKE','MotorBike')])

class Bookings(models.Model):
	status=models.CharField(max_length=20,choices=[('CANCELLED','Cancelled'),('COMPLETED','Completed'),('TOBECOMPLETED','ToBeCompleted')])
	start_date=models.DateField()
	end_date=models.DateField()
	km_drove=models.IntegerField()
	cost=models.IntegerField()
	borrower=models.OneToOneField(Borrower,null=True,on_delete=models.CASCADE)
	lender=models.OneToOneField(Lender,null=True,on_delete=models.CASCADE)
	vehicle=models.OneToOneField(Vehicle,on_delete=models.CASCADE)	
