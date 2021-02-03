from rest_framework import serializers

from .models import Doctor, Language, Category, Location, District

class LangungeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Language
    fields = ['id', 'label']

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'label']

class DistrictSerializer(serializers.ModelSerializer):
  class Meta:
    model = District
    fields = ['id', 'label']

class LocationSerializer(serializers.ModelSerializer):
  district = DistrictSerializer()
  
  class Meta:
    model = Location
    fields = ['id', 'label','address','district']

class DoctorSerializer(serializers.ModelSerializer):
  languages = LangungeSerializer(many=True)
  categories = CategorySerializer(many=True)
  locations = LocationSerializer(many=True)

  class Meta:
    model = Doctor
    fields = ['id', 'doctor_id', 'name', 'chi_name', 'languages', 'categories', 'locations']
