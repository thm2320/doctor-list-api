from rest_framework import serializers

from .models import Doctor, Language, Category

class LangungeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Language
    fields = ['id', 'label']

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'label']

class DoctorSerializer(serializers.ModelSerializer):
  languages = LangungeSerializer(many=True)
  categories = CategorySerializer(many=True)

  class Meta:
    model = Doctor
    fields = ['id', 'doctor_id', 'name', 'chi_name', 'languages', 'categories']
