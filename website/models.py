from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    

     first_name =models.CharField( max_length=50)
     last_name =models.CharField( max_length=50)
     email =models.EmailField( max_length=254, blank=True, null=True)
     phone_numer= models.CharField(max_length=20)
     city =models.CharField( max_length=50)
     created_by = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    

     def __str__(self):
            return self.first_name 
    
