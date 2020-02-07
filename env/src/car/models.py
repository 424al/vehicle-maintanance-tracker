from django.db import models


class Vehicle(models.Model):
	#VEHICLE INFORMATION
	year = models.IntegerField(blank=False, null=True)
	make = models.CharField(blank=False,max_length=300)
	model = models.CharField(blank=False,max_length=300)
	license_plate = models.CharField(max_length=300, blank=False,null=True)
	car_id = models.CharField(blank=False, null=True, max_length=300)

	class Meta:
		abstract=True


class Services(Vehicle):
	date = models.IntegerField(blank=False, null=True)
	info = models.TextField(max_length=5000,blank=False)
