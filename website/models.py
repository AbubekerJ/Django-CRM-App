from django.db import models


# Create your models here.

class Customer(models.Model):
    

     first_name =models.CharField( max_length=50)
     last_name =models.CharField( max_length=50)
     email =models.EmailField( max_length=254, blank=True, null=True)
     phone_numer= models.CharField(max_length=20)
     city =models.CharField( max_length=50)
    

     def __str__(self):
            return self.first_name 
    
