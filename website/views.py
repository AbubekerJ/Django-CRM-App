from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate ,login, logout
from django.contrib import messages
from .forms import SignUpForm ,AddCustomer
from .models import Customer
# Create your views here.

def home(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request , username=username , password = password )
        
        if user is not None:
            login(request, user)
            messages.success(request , 'You Have Loged In Succesfully ')
            return redirect('home')
        else :
            messages.success(request, 'Invalid user. If You Dont have Account Register First To Continue!')
            return redirect('home')


    else:  
        

        customers = Customer.objects.all()
       
        
        return render (request , 'home.html', {'customers':customers})

def log_out(request):
        logout(request) 
        messages.success(request , 'You have been Loged Out')
        return redirect('home')


        
    
def register(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , 'You have registered successfully')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def customer(request , pk):
    if request.user.is_authenticated:
        the_customer  = Customer.objects.get(id=pk)
        return render (request , 'customer.html',{'the_customer':the_customer})
    else:
        messages.success(request , 'You need to log in Frst ')
        return redirect ('home')
    
def delete_customer(request ,pk):
    if request.user.is_authenticated:
        delete_cu =  Customer.objects.get(id=pk)
        delete_cu.delete()
        messages.success(request , 'You deleted the recorde succusfully ')
        return redirect ('home')
    else:
        messages.success(request , 'You need to log in To delet the Records ')
        return redirect('home')
        

def add_customer(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = AddCustomer(request.POST)
            if form.is_valid():
                
                customer = form.save(commit=False)
                customer.created_by = request.user  
                customer.save()
                messages.success(request , 'You have Added Customer successfully')
                return redirect('home')
        else:
            form = AddCustomer()
        return render(request, 'add_customer.html', {'form': form})
    else:
        messages.success(request , 'You need to log in To Add the Records ')
        return redirect('home')

    
def update_customer(request, pk):
    if request.user.is_authenticated:
          update_customer = Customer.objects.get(id=pk)
          form = AddCustomer(request.POST or None , instance= update_customer)
          if form.is_valid():
                form.save()
                messages.success(request , 'Record Updated Succesfully ')
                return redirect('home')
          else:
              form = AddCustomer(request.POST or None , instance= update_customer)
              return render (request , 'update_customer.html',{'form':form , })
            
          
