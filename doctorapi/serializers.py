from rest_framework import serializers

from .models import Doctor, Language

class LangungeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Language
    fields = ['id', 'label']

class DoctorSerializer(serializers.ModelSerializer):
  languages = LangungeSerializer(many=True)

  class Meta:
    model = Doctor
    fields = ['id', 'doctor_id', 'name', 'chi_name', 'languages']
