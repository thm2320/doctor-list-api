from rest_framework import viewsets

from .serializers import DoctorSerializer
from .models import Doctor


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('name')
    serializer_class = DoctorSerializer