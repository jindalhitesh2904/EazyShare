from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Person(models.Model):
	user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
	first_name=models.CharField(max_length=100,default="")
	last_name=models.CharField(max_length=100,default="")
	email=models.EmailField(max_length=250,null=True)
	phone=PhoneNumberField(null=True)
	address=models.TextField(max_length=250,default="None")
	age=models.IntegerField(null=True)
	profile_pic=models.ImageField(upload_to='images',default="images/iitbhu.png")
	def __str__(self):
		return self.first_name+self.last_name

class Vehicle(models.Model):
	brand_name=models.CharField(max_length=100)
	model_name=models.CharField(max_length=100,null=True)
	registration_number=models.CharField(max_length=100,null=True)
	year=models.IntegerField()
	description=models.TextField()
	category=models.CharField(max_length=20,choices=[('CAR','Car'),('SCOOTY','Scooty'),('MOTORBIKE','MotorBike')])
	km_driven=models.PositiveIntegerField()

	pic=models.ImageField(upload_to='images',default="images/iitbhu.png")

	owner=models.ForeignKey(Person,on_delete=models.CASCADE)
	def __str__(self):
		return self.model_name

class Bookings(models.Model):
	status=models.CharField(max_length=20,choices=[('CANCELLED','Cancelled'),('COMPLETED','Completed'),('TOBECOMPLETED','ToBeCompleted')])
	start_date=models.DateField()
	end_date=models.DateField()
	km_drove=models.IntegerField()
	cost=models.IntegerField()
	borrower=models.OneToOneField(Person,null=True,on_delete=models.CASCADE)
	lender=models.OneToOneField(Person,null=True,on_delete=models.CASCADE,related_name='+')
	vehicle=models.OneToOneField(Vehicle,on_delete=models.CASCADE)	
	
