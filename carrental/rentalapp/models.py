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
	profile_pic=models.ImageField(blank=True,default="iitbhu.jpeg")
	def __str__(self):
		return self.first_name+self.last_name
		

class Vehicle(models.Model):
	brand_name=models.CharField(max_length=100)
	model_name=models.CharField(max_length=100,null=True)
	registration_number=models.CharField(max_length=100,null=True)
	year=models.IntegerField()
	description=models.TextField()
	category=models.CharField(max_length=20,choices=[('Car','Car'),('Scooty','Scooty'),('Motorbike','Motorbike')])
	km_driven=models.PositiveIntegerField()

	pic=models.ImageField(blank=True,default="iitbhu.jpeg")

	owner=models.ForeignKey(Person,on_delete=models.CASCADE)
	def __str__(self):
		return self.model_name

class Bookings(models.Model):
	status=models.CharField(max_length=20,choices=[('COMPLETED','COMPELETED'),('BOOKED','BOOKED'),('AVAILABLE','AVAILABLE')], default='AVAILABLE')
	start_date=models.DateField(null=True)
	end_date=models.DateField(null=True)
	per_km_cost=models.PositiveIntegerField(default=12)
	per_day_cost=models.PositiveIntegerField(default=500)
	km_drove=models.IntegerField(null=True)
	cost=models.IntegerField(null=True)
	borrower=models.ForeignKey(Person,null=True,on_delete=models.CASCADE)
	lender=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='+')
	vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
	def __str__(self):
		if self.id == None:
			return 'ABCD'
		return str(self.id)