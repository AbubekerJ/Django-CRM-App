
from django.urls import path 

from .import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('log_out', views.log_out , name = 'log_out'),
    path('register', views.register, name ='register'),
    path('add_customer', views.add_customer, name ='add_customer'),
    path('customer/<int:pk>', views.customer, name ='customer'),
    path('delete_customer/<int:pk>', views.delete_customer, name ='delete_customer'),
    path('update_customer/<int:pk>', views.update_customer, name ='update_customer'),
    
  
    
    
]
