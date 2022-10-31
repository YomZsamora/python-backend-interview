from django.urls import path

from . import views

app_name = 'trips'

urlpatterns = [
    # GET: /Fetch All Drivers List
    path('drivers/', views.DriverView.as_view(), name='drivers-list'),
    # GET: /Fetch All Customers List
    path('customers/', views.CustomerView.as_view(), name='customers-list'),
    # GET: /Fetch All Vehicles List
    path('vehicles/', views.VehicleView.as_view(), name='vehicles-list'),
    # GET: /Fetch All Trips Recorded
    path('trips/', views.TripList.as_view(), name='trip-list'),
    # POST: /Add a New Trip to the Records
    path('trip/add/', views.TripCreate.as_view(), name="create-trip"),
    # GET: /Fetched a Specific Trip Given the ID
    path('trip/<int:pk>/', views.TripDetail.as_view(), name='trip-details'),
    # POST: /Logs User In after Successful Authentication   
    path('login/', views.LoginView.as_view(), name='login'),
    # POST: /Registers a New User 
    path('register/', views.RegisterUserAPIView.as_view(), name='register'),
]
