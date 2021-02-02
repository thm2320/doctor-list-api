from rest_framework import serializers

from .models import Doctor

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name', 'doctor_id')