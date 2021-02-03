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

class Doctor(models.Model):
  doctor_id = models.CharField(max_length=60)
  name = models.CharField(max_length=60)
  chi_name = models.CharField(max_length=60, null=True)
  languages = models.ManyToManyField(Language)
  categories = models.ManyToManyField(Category)
    
  def __str__(self):
    return self.name

