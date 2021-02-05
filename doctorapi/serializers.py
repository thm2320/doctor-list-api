from rest_framework import serializers

from .models import Doctor, Language, Category, Location, District, Service, OperationSchedule

class LanguageSerializer(serializers.ModelSerializer):
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
    fields = ['string_id', 'label']

class LocationSerializer(serializers.ModelSerializer):
  district = DistrictSerializer()
  
  class Meta:
    model = Location
    fields = ['id', 'label','address','district']

class OperationScheduleSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = OperationSchedule
    fields = ['days','times']

class ServiceSerializer(serializers.ModelSerializer):
  operation_schedules = OperationScheduleSerializer(many=True)
  category = CategorySerializer()
  
  class Meta:
    model = Service
    fields = ['id', 'label', 'price', 'priceDetails', 'operation_schedules', 'category']

class DoctorSerializer(serializers.ModelSerializer):
  languages = LanguageSerializer(many=True)  
  locations = LocationSerializer(many=True)
  service_set = ServiceSerializer(many=True)

  class Meta:
    model = Doctor
    fields = ['id', 'doctor_id', 'name', 'chi_name', 'languages', 'locations', 'service_set']
