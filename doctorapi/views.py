from doctorapi.models import Doctor
from doctorapi.serializers import DoctorSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DoctorList(APIView):
  def get(self, request, format=None):
    language = self.request.query_params.get('language', None)

    doctors = Doctor.objects.all()
    if language is not None:
      doctors = doctors.filter(languages__label=language)
    
    serializer = DoctorSerializer(doctors, many=True)    
    return Response(serializer.data)

  # def post(self, request, format=None):
  #   serializer = DoctorSerializer(data=request.data)
  #   if serializer.is_valid():
  #     serializer.save()
  #     return Response(serializer.data, status=status.HTTP_201_CREATED)
  #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorDetail(APIView):
  def get_object(self, id):
    try:
      return Doctor.objects.get(id=id)
    except Doctor.DoesNotExist:
      raise Http404

  def get(self, request, id, format=None):
    doctor = self.get_object(id)
    serializer = DoctorSerializer(doctor)
    return Response(serializer.data)

  # def put(self, request, id, format=None):
  #   doctor = self.get_object(id)
  #   serializer = DoctorSerializer(doctor, data=request.data)
  #   if serializer.is_valid():
  #     serializer.save()
  #     return Response(serializer.data)
  #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  # def delete(self, request, id, format=None):
  #   doctor = self.get_object(id)
  #   doctor.delete()
  #   return Response(status=status.HTTP_204_NO_CONTENT)
