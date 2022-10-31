from django.db import models


# Driver Model
class Driver(models.Model):
    last_name = models.CharField(max_length=50, blank=False, help_text="Last_Name.")
    first_name = models.CharField(max_length=50, blank=False, help_text="First_Name.")
    email_address = models.EmailField(max_length=50, unique=True)
    phone_number = models.IntegerField(blank=False)
    
    def __str__(self):
        return self.email_address

# Vehicles Model
class Vehicle(models.Model):
    model_type = models.CharField(max_length=70, blank=False)
    available = models.BooleanField()
    
    def __str__(self):
        return self.model_type
   
# Customer Model    
class Customer(models.Model):
    last_name = models.CharField(max_length=50, blank=False, help_text="Last_Name.")
    first_name = models.CharField(max_length=50, blank=False, help_text="First_Name.")
    address = models.CharField(max_length=150, blank=False)
    phone_number = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

# AddressTypes
class AddressTypes(models.TextChoices):
    PICKUP_POINT = 'pickup_point'
    DROP_OFF_POINT = 'drop_off_point'

# Trips Model    
class Trip(models.Model):
    driver_id = models.ForeignKey(Driver, null=False, on_delete=models.CASCADE )
    vehicle_id = models.ForeignKey(Vehicle, null=False, on_delete=models.CASCADE )
    customer_id = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE )
    address = models.CharField(max_length=50, blank=False)
    cargo_tonnage = models.DecimalField(max_digits=10, decimal_places=2)
    address_type = models.CharField(max_length=50, choices = AddressTypes.choices, default=AddressTypes.PICKUP_POINT)
    done_by_user_id = models.ForeignKey('auth.user', related_name="trip", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


