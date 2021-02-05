from django.test import TestCase
from doctorapi.models import *
from doctorapi.serializers import *

class LangugeSerializerTestCase(TestCase):
  def setUp(self):
    test_lang = Language.objects.create(
      label="English"
    )
    self.expected_data = { 
      'id': 1,
      'label': "English"     
    }  
    
    self.test_lang=test_lang

  def test_language_data(self):
    serializer = LanguageSerializer(instance=self.test_lang)    
    test_data = serializer.data
    self.assertEqual(test_data, self.expected_data)

class CategoryAndServiceSerializerTestCase(TestCase):
  def setUp(self):
    test_category = Category.objects.create(
      label="Cat 1"
    )
    test_service = Service.objects.create(
      category=test_category,
      label="Service 1",
      price=150,
      priceDetails="Medicine included"
    )
    self.expected_category_data = { 
      'id': 1,
      'label': "Cat 1" 
    }  
    self.expected_service_data = { 
      'id': 1,
      'label': "Service 1",
      'price': "150.00",
      'priceDetails': "Medicine included",
      'category':self.expected_category_data,
      'operation_schedules':[]
    }  
    
    self.test_category=test_category
    self.test_service=test_service

  def test_category_data(self):
    serializer = CategorySerializer(instance=self.test_category)    
    test_data = serializer.data
    self.assertEqual(test_data, self.expected_category_data)
  
  def test_service_data(self):
    serializer = ServiceSerializer(instance=self.test_service)    
    test_data = serializer.data
    self.assertEqual(test_data, self.expected_service_data)

class DistrictAndLocationSerializerTestCase(TestCase):
  def setUp(self):
    test_district = District.objects.create(
      string_id="kwun-tong",
      label="Kwun Tong",
    )    

    test_location = Location.objects.create(
      label="clinic 001",
      address="No 1, Street 2, Place 3",
      district=test_district
    )

    self.expected_district_data = { 
      'string_id': "kwun-tong",
      'label': "Kwun Tong"
    }  
    self.expected_location_data = { 
      'id': 1,
      'address': "No 1, Street 2, Place 3",
      'label': "clinic 001",
      'district': self.expected_district_data
    }  
    
    self.test_district=test_district
    self.test_location=test_location

  def test_district_data(self):
    serializer = DistrictSerializer(instance=self.test_district)    
    test_data = serializer.data
    self.assertEqual(test_data, self.expected_district_data)

  def test_location_data(self):
    serializer = LocationSerializer(instance=self.test_location)    
    test_data = serializer.data
    self.assertEqual(test_data, self.expected_location_data)

class DoctorSerializerTestCase(TestCase):

  def setUp(self):
    test_doctor = Doctor.objects.create(
      doctor_id= "TEST001", 
      name= "Dr. Test",
      chi_name= "試醫生",
    )

    test_lang = Language.objects.create(
      label="English"
    )
    test_doctor.languages.add(test_lang)
    test_doctor.save()

    

    test_district = District.objects.create(
      string_id="sha-tin",
      label="Sha Tin"
    )
    test_district.save()

    test_location = Location.objects.create(
      label="clinic 001",
      address="No 1, Street 2, Place 3",
      district=test_district
    )
    test_location.save()

    test_doctor.locations.add(test_location)
    test_doctor.save()    

    test_category1 = Category.objects.create(
      label="cat1"
    )
    test_category2 = Category.objects.create(
      label="cat2"
    )
    test_doctor.save()
    test_service = Service.objects.create(
      category=test_category1,
      doctor=test_doctor,
      label="Service 1",
      price=199,
      priceDetails="(medicine not included)",
    )

    self.test_doctor = test_doctor
    self.expected_data = {
      'doctor_id': "TEST001", 
      'name': "Dr. Test",
      'chi_name': "試醫生",
      'languages': [{
        'label': "English"
      }],
      'categories': [{
        'label': "cat1"
      },{
        'label': "cat2"
      }],
      'locations': [{
        'label': "clinic 001",
        'address': "No 1, Street 2, Place 3"
      }],
      'service_set': [{
        'label':"Service 1",
        'price':"199.00",
        'priceDetails':"(medicine not included)"
      }]
    }  

  def test_doctor_primitive_data(self):
    serializer = DoctorSerializer(instance=self.test_doctor)
    test_data = serializer.data
    self.assertEqual(test_data['doctor_id'], self.expected_data['doctor_id'])
    self.assertEqual(test_data['name'], self.expected_data['name'])
    self.assertEqual(test_data['chi_name'], self.expected_data['chi_name'])

  def test_doctor_languages_relation(self):
    serializer = DoctorSerializer(instance=self.test_doctor)
    test_data = serializer.data
    self.assertEqual(len(test_data['languages']), len(self.expected_data['languages']))
    self.assertEqual(test_data['languages'][0]['label'], self.expected_data['languages'][0]['label'])  
  
  def test_doctor_locations_relation(self):
    serializer = DoctorSerializer(instance=self.test_doctor)
    test_data = serializer.data
    self.assertEqual(len(test_data['locations']), len(self.expected_data['locations']))
    self.assertEqual(test_data['locations'][0]['label'], self.expected_data['locations'][0]['label'])
    self.assertEqual(test_data['locations'][0]['address'], self.expected_data['locations'][0]['address'])

  def test_doctor_services_relation(self):
    serializer = DoctorSerializer(instance=self.test_doctor)
    test_data = serializer.data
    self.assertEqual(len(test_data['service_set']), len(self.expected_data['service_set']))
    self.assertEqual(test_data['service_set'][0]['label'], self.expected_data['service_set'][0]['label'])
    self.assertEqual(test_data['service_set'][0]['price'], self.expected_data['service_set'][0]['price'])
    self.assertEqual(test_data['service_set'][0]['priceDetails'], self.expected_data['service_set'][0]['priceDetails'])