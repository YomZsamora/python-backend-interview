from django.shortcuts import render
from .models import Driver, Customer, Vehicle, Trip

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import DriverSerializer, CustomerSerializer, VehicleSerializer, TripSerializer, UserSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.contrib.auth.models import User

# New User Registration
class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
  
    def get(self,request,*args,**kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# User Log in Authentication
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'message': 'User Logged In Successfully!'}, status=status.HTTP_200_OK)
    
    def get(self, request):
        content = {"user": str(request.user), "auth": str(request.auth)}
        return Response(data=content, status=status.HTTP_200_OK)
    

# Fetches All Drivers 
class DriverView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response({"drivers": serializer.data}, status=status.HTTP_200_OK)

# Fetches All Customers
class CustomerView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response({"customers": serializer.data}, status=status.HTTP_200_OK)

# Fetches All Vehicles
class VehicleView(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response({"vehicles": serializer.data}, status=status.HTTP_200_OK)

# Fetches All Trips    
class TripList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response({"trips": serializer.data}, status=status.HTTP_200_OK)

# Creates a New Trip Object
class TripCreate(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Retrieves a Specific Trip given the Trip's ID. Updates and Deletes as Well.      
class TripDetail(APIView):
    
    def get_trip_by_pk(self, pk):
        try:
            return Trip.objects.get(pk=pk)
        except:
            return Response({"error": "Trip does not exist!"}, status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        trip = self.get_trip_by_pk(pk)
        serializer = TripSerializer(trip)
        return Response(serializer.data)
    
    def put(self, request, pk):
        trip = self.get_trip_by_pk(pk)
        serializer = TripSerializer(trip, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        trip = self.get_trip_by_pk(pk)
        trip.delete()
        return Response({"messages": "Selected Trip Has Beed Deleted!"}, status=status.HTTP_204_NO_CONTENT)