# Introduction

* Aim to practice coding using Python. 
* Build an api server using Django and Django Rest Framework
* The model design is based on this https://drive.google.com/file/d/1DLVZmKLiWsTMPUIGw-EHL9Grv9REgG3a/view?usp=sharing

# Create virtual environment and install libraries for the project

1. run cmd `"py -m venv env"` to create a virtual environment
1. activate the virtual environment just created
1. run cmd `"pip install -r requirements.txt"` to install the libraries

# To run local server

1. run cmd `"py manage.py migrate"` to initize the database for the project
1. run cmd `"py manage.py createsuperuser"` and follow instruction to create super user
1. run cmd `"py manage.py runserver"` to start up the local server
1. open broswer and go to http://127.0.0.1:8000/admin/
1. login as super user and create the doctor data
1. go to http://127.0.0.1:8000/doctor/ , should get a list of doctor. 
1. It also accept "language", "district", "category", "price_range" as filter. e.g. http://127.0.0.1:8000/doctor?language=English&district=sha-tin&category=cat1&price_range=100,199
1. go to http://127.0.0.1:8000/doctor/{id} . should get a doctor info by specified id

# To run unittest for views and serializers

1. run cmd `"py manage.py test"`