from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Driver, Customer, Vehicle, Trip
from django.contrib.auth.models import User
# from .factories import CustomerFactory

# class to define a test case of login
class AuthenticateUserTestcase(APITestCase):
    

    def test_registered_user_created_in_successfully(self):
        reg_data = { "username": "myusername", "email": "myemail@mydomain.com", "password": "mypassword123", "password2": "mypassword123", "first_name": "myfirstname", "last_name": "mylastname" }
        response = self.client.post(reverse('trips:register'), reg_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_registered_user_can_log_in_successfully(self):
        reg_data = { "username": "myusername", "email": "myemail@mydomain.com", "password": "mypassword123", "password2": "mypassword123", "first_name": "myfirstname", "last_name": "mylastname" }
        self.client.post(reverse('trips:register'), reg_data)
        
        login_data = {"username": "myusername", "password": "mypassword123" }
        response = self.client.post(reverse('trips:login'), login_data)
        
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response.data['token']}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_password_fields_match_validation(self):
        reg_data = { "username": "myusername", "email": "myemail@mydomain.com", "password": "mypassword123", "password2": "myotherpassword123", "first_name": "myfirstname", "last_name": "mylastname" }
        response = self.client.post(reverse('trips:register'), reg_data)
        self.assertEqual(response.json()['password'], ["Password fields didn't match."])
        
        
class TripViewSetTestCase(APITestCase):
    
    def setup(self):
        reg_data = { "username": "myusername", "email": "myemail@mydomain.com", "password": "mypassword123", "password2": "mypassword123", "first_name": "myfirstname", "last_name": "mylastname" }
        self.client.post(reverse('trips:register'), reg_data)
        
        login_data = {"username": "myusername", "password": "mypassword123" }
        response = self.client.post(reverse('trips:login'), login_data)
        
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response.data['token']}")
        
    def test_trip_list_authenticated(self):
        self.setup()
        response = self.client.get(reverse('trips:trip-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_trip_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('trips:trip-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_post_new_trip_item(self):
        self.setup()
        test_driver = Driver.objects.create(last_name="samora", first_name="adzumi", email_address="lytahlaurah@gmail.com", phone_number=710657696)
        test_vehicle = Vehicle.objects.create(model_type="Volvo FH16 (2012)", available=True)
        test_customer = Customer.objects.create(last_name="Muturi", first_name="Peter", address="peter.muturi@gmail.com", phone_number=710657696)
        test_user = User.objects.create(username="yomz", password="samora90", email="samora90@gmail.com", last_name="samora", first_name="Yommie")
        
        trip = {
            "address": "Kajanta Rd, Waiyaki Way",
            "cargo_tonnage": "345.01",
            "address_type": "drop_off_point",
            "driver_id": test_driver.id,
            "vehicle_id": test_vehicle.id,
            "customer_id": test_customer.id,
            "done_by_user_id": test_user.id
        }
        response = self.client.post(reverse('trips:create-trip'), trip, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_post_new_trip_item_error(self):
        self.setup()
        trip = {}
        response = self.client.post(reverse('trips:create-trip'), trip, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    #drivers test
    def test_post_new_driver_item(self):
        self.setup()
        driver = {
            "last_name": "Galina",
            "first_name": "Lorraine",
            "email_address": "lytahlaurah@gmail.com",
            "phone_number": 710657696
        }
        response = self.client.post(reverse('trips:create-driver'), driver)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_post_new_driver_item_error(self):
        self.setup()
        driver = {}
        response = self.client.post(reverse('trips:create-driver'), driver)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
           
    def test_drivers_list_retrieve(self):
        self.setup()
        response = self.client.get(reverse('trips:drivers-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_customers_list_retrieve(self):
        self.setup()
        response = self.client.get(reverse('trips:customers-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_vehicles_list_retrieve(self):
        self.setup()
        response = self.client.get(reverse('trips:vehicles-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # Models
    def test_class_drivers(self):
        self.setup()
        test_driver = Driver.objects.create(last_name="samora", first_name="adzumi", email_address="lytahlaurah@gmail.com", phone_number=710657696)
        self.assertEqual(str(test_driver), test_driver.email_address)
        
    def test_class_vehicle(self):
        self.setup()
        test_vehicle = Vehicle.objects.create(model_type="Volvo FH16 (2012)", available=True)
        self.assertEqual(str(test_vehicle), test_vehicle.model_type)
        
    def test_class_customer(self):
        self.setup()
        test_customer = Customer.objects.create(last_name="Muturi", first_name="Peter", address="peter.muturi@gmail.com", phone_number=710657696)
        self.assertEqual(str(test_customer), test_customer.first_name + " " + test_customer.last_name)
        
    def test_trips_list_retrieve(self):
        self.setup()
        response = self.client.get(reverse('trips:trip-details', kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
        
