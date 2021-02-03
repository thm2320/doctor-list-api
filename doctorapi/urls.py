from django.urls import include, path
from rest_framework import routers
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
  path('doctor/', views.DoctorList.as_view()),
  path('doctor/<int:id>', views.DoctorDetail.as_view()),
  # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]