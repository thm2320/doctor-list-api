from doctorapi.models import Doctor,District,Category,Service
from doctorapi.serializers import DoctorSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DoctorList(APIView):
  def get(self, request, format=None):
    language = self.request.query_params.get('language', None)
    category = self.request.query_params.getlist('category', None)
    district = self.request.query_params.getlist('district', None)
    price_range = self.request.query_params.get('price_range', None)
    
    doctors = Doctor.objects.all()
    if language:
      doctors = doctors.filter(languages__label=language)
    if district:
      distEntries = District.objects.filter(string_id__in=district)
      doctors = doctors.filter(locations__district__in=distEntries).distinct()
    if category and price_range:
      catEntries = Category.objects.filter(label__in=category)
      min_price,max_price = price_range.split(',')
      doctors = doctors.filter(
        service__category__in=catEntries,
        service__price__range=(min_price,max_price)
      ).distinct()
    elif category:
      catEntries = Category.objects.filter(label__in=category)
      doctors = doctors.filter(service__category__in=catEntries).distinct()
    elif price_range:
      min_price,max_price = price_range.split(',')
      doctors = doctors.filter(service__price__range=(min_price,max_price)).distinct()

    serializer = DoctorSerializer(doctors, many=True)    
    return Response(serializer.data)

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