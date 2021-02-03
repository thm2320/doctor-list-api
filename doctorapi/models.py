from django.db import models

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

