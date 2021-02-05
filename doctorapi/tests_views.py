from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from doctorapi.models import *
from .views import * 

class DoctorViewTestCases(APITestCase):
  def setUp(self):
    test_doctor_1 = Doctor.objects.create(
      doctor_id= "TEST001", 
      name= "Test 1",
      chi_name= "試醫生一",
    )

    test_doctor_2 = Doctor.objects.create(
      doctor_id= "TEST002", 
      name= "Test 2",
      chi_name= "試醫生二",
    )

    test_lang_en = Language.objects.create(
      label="English"
    )
    test_lang_ca = Language.objects.create(
      label="廣東話"
    )
    test_doctor_1.languages.add(test_lang_en,test_lang_ca)
    test_doctor_2.languages.add(test_lang_ca)    

    test_district_st = District.objects.create(
      string_id="sha-tin",
      label="Sha Tin"
    )
    test_district_kt = District.objects.create(
      string_id="kwun-tong",
      label="Kwun Tong"
    )
    test_district_tws = District.objects.create(
      string_id="wong-tai-sin",
      label="Wong Tai Sin"
    )

    test_location_c1 = Location.objects.create(
      label="clinic 001",
      address="No 1, Street 1, Place 1",
      district=test_district_st
    )
    test_location_c2 = Location.objects.create(
      label="clinic 002",
      address="No 2, Street 2, Place 2",
      district=test_district_kt
    )
    test_doctor_1.locations.add(test_location_c1)
    test_doctor_2.locations.add(test_location_c2)  

    test_category1 = Category.objects.create(
      label="cat1"
    )
    test_category2 = Category.objects.create(
      label="cat2"
    )  

    test_service_1a = Service.objects.create(
      category=test_category1,
      doctor=test_doctor_1,
      label="Service 1a",
      price=199,
      priceDetails="(medicine not included)",
    )
    test_service_1b = Service.objects.create(
      category=test_category2,
      doctor=test_doctor_1,
      label="Service 1b",
      price=300,
      priceDetails="(medicine included)",
    )
    test_service_2a = Service.objects.create(
      category=test_category1,
      doctor=test_doctor_2,
      label="Service 2a",
      price=250,
      priceDetails="",
    )

    test_doctor_1.save()
    test_doctor_2.save()

    self.factory = APIRequestFactory()

  #DoctorList Start=================================================
  #list without any filters
  def test_doctor_list_all(self):    
    request = self.factory.get('/doctor')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),2)

  #filter by language
  def test_doctor_list_lang_1_match(self):    
    request = self.factory.get('/doctor?language=English')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),1)
  
  def test_doctor_list_lang_2_match(self):    
    request = self.factory.get('/doctor?language=廣東話')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),2)

  def test_doctor_list_lang_no_match(self):    
    request = self.factory.get('/doctor?language=some_lang')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),0)

  #filter by district
  def test_doctor_list_district_1_match(self):    
    request = self.factory.get('/doctor?district=kwun-tong')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),1)

  def test_doctor_list_district_multi_select(self):    
    request = self.factory.get('/doctor?district=kwun-tong&district=sha-tin')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),2)

  def test_doctor_list_district_no_match(self):    
    request = self.factory.get('/doctor?district=wong-tai-sin')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),0)

  #filter by price range
  def test_doctor_list_price_1_match(self):    
    request = self.factory.get('/doctor?price_range=100,199')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),1)

  def test_doctor_list_price_2_match(self):    
    request = self.factory.get('/doctor?price_range=199,250')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),2)

  def test_doctor_list_price_no_match(self):    
    request = self.factory.get('/doctor?price_range=251,299')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),0)

  #filter by category
  def test_doctor_list_category_1_match(self):    
    request = self.factory.get('/doctor?category=cat2')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),1)

  def test_doctor_list_category_2_match(self):    
    request = self.factory.get('/doctor?category=cat1')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),2)

  def test_doctor_list_category_multi_select(self):    
    request = self.factory.get('/doctor?category=cat1&category=cat2')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),2)

  def test_doctor_list_category_no_match(self):    
    request = self.factory.get('/doctor?category=cat4')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),0)

  #filter by category and price_range
  #cat1: $199, $250
  #cat2: $300
  def test_doctor_list_catAndPrice_1_match(self):    
    request = self.factory.get('/doctor?category=cat1&price_range=100,199')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),1)

  def test_doctor_list_catAndPrice_2_match(self):    
    request = self.factory.get('/doctor?category=cat1&price_range=199,250')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),2)

  def test_doctor_list_catAndPrice_no_match(self):    
    request = self.factory.get('/doctor?category=cat2&price_range=199,250')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),0)

  #filter by mixed criteria
  def test_doctor_list_mixed_1_match(self):    
    request = self.factory.get('/doctor?language=廣東話&district=sha-tin&category=cat1&price_range=100,199')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),1)

  def test_doctor_list_mixed_no_match(self):    
    request = self.factory.get('/doctor?language=English&district=sha-tin&category=cat1&price_range=100,199')
    view = DoctorList.as_view()
    response = view(request)
    self.assertEqual(len(response.data),1)
  #DoctorList End=================================================

  #DoctorDetail Start================================================= 
  def test_doctor_view_existing(self):    
    request = self.factory.get('/doctor')
    view = DoctorDetail.as_view()
    response = view(request,1)
    self.assertEqual(response.data['id'],1)
    self.assertEqual(response.data['doctor_id'],'TEST001')
    self.assertEqual(response.data['name'],'Test 1')

  def test_doctor_view_not_existing(self):    
    request = self.factory.get('/doctor')
    view = DoctorDetail.as_view()
    response = view(request,10)
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
  #DoctorDetail End=================================================

    