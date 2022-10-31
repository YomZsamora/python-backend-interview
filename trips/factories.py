import factory
import factory.fuzzy

from .models import Customer

class CustomerFactory(factory.django.DjangoModelFactory):

    class Meta: 
        model = Customer
    
    last_name = factory.Faker("name")
    first_name = factory.Faker("name")
    address = factory.Faker("address")
    phone_number = factory.Faker("phone_number")