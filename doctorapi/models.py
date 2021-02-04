from django.db import models
import uuid

# Create your models here.
class Language(models.Model):
  label = models.CharField(max_length=60)

  def __str__(self):
    return self.label

class Category(models.Model):    
  label = models.CharField(max_length=60)
  
  def __str__(self):
    return self.label

class District(models.Model):
  string_id = models.CharField(max_length=60, unique=True, default=uuid.uuid4)
  label = models.CharField(max_length=60)
  
  def __str__(self):
    return self.label

class Location(models.Model):
  label = models.CharField(max_length=60)
  address = models.TextField(null=True)
  district = models.ForeignKey(District, null=True, on_delete=models.PROTECT)
  phone = models.CharField(max_length=60, null=True)
  
  def __str__(self):
    return self.label

class Doctor(models.Model):
  doctor_id = models.CharField(max_length=60)
  name = models.CharField(max_length=60)
  chi_name = models.CharField(max_length=60, null=True)
  languages = models.ManyToManyField(Language)
  categories = models.ManyToManyField(Category)
  locations = models.ManyToManyField(Location)
    
  def __str__(self):
    return self.name

class OperationSchedule(models.Model):
  days = models.CharField(max_length=255) # eg. "Monday, Wednesday"
  times = models.CharField(max_length=255) # eg. "9am to 12nn, 3pm to 6pm" 

  def __str__(self):
    return self.days + ': ' + self.times

class Service(models.Model):
  doctor = models.ForeignKey(Doctor, null=True, on_delete=models.PROTECT)
  label = models.CharField(max_length=60)
  price = models.DecimalField(max_digits=19, decimal_places=2)
  priceDetails = models.TextField(null=True)
  operation_schedules = models.ManyToManyField(OperationSchedule)

  def __str__(self):
    return self.label 

