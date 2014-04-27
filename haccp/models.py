from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
    
class Technician(models.Model):
    user=models.OneToOneField(User)
    is_tech=models.BooleanField(True)

class Manager(models.Model):
    user=models.OneToOneField(User)
    is_manager=models.BooleanField(True)
    manager_name=models.CharField(max_length=10)
# Create your models here.

class QuatForm(models.Model):
    date =models.DateField(auto_now_add=True)
    techincian_name = models.CharField(max_length = 255, verbose_name='Technician Name')
    technician_initial = models.CharField(max_length = 5) #initial is done in the check field of the actual form
    manager_name = models.CharField(max_length =255,blank=True) #manager when checking
    manager_initial = models.CharField(max_length = 5,blank=True) #same as technician initial - perform as digital signature
    is_reviewed_date =models.DateField(auto_now=True, blank=True) #set to null because this would be updated the next day
    is_reviewed = models.CharField(max_length =5, blank=True) #same as technician initial - perform as digital signature
    hand_pallet_sanitizer_strength = models.CharField(max_length=10,verbose_name="Hand Pallet Sanitizer Strength")
    footbath1_sanitizer_strength = models.CharField(max_length=10,verbose_name="Footbath 1 Sanitizer Strength")
    footbath2_sanitizer_strength = models.CharField(max_length=10,verbose_name="Footbath 2 Sanitizer Strength")
    footbath3_sanitizer_strength = models.CharField(max_length=10,verbose_name="Footbath 3 Sanitizer Strength")
    footbath4_sanitizer_strength = models.CharField(max_length=10,verbose_name="Footbath 4 Sanitizer Strength")
    footbath5_sanitizer_strength = models.CharField(max_length=10,verbose_name="Footbath 5 Sanitizer Strength")
    assembly_sanitizer_strength  = models.CharField(max_length=10,verbose_name="Assembly Conveyor Sanitizer Strength")