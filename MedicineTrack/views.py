<<<<<<< HEAD
from django.shortcuts import render,redirect
from django.http import HttpResponse
from MedicineTrack.models import Retail,Contact
from .forms import FormRetail
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'medicine/index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return HttpResponse("<h1>Thanks for contact us</h1>")
    return render(request, 'contact.html')

def RetailDetails(request):
    retaildetails = Retail.objects.all()
    return render(request,'retail.html',{'Retail':retaildetails})
       

def addRetail(request):
    if request.method == 'POST':
        form = FormRetail(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('RetailDetails')
    else:
        form = FormRetail()
    return render(request, 'addretail.html',{'form':form})


=======
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from .forms import RetailForm
from django.contrib.auth.models import User
from .models import Medicine,MedicinePrice
from django.core.cache import cache
from .models import *
from django.http import JsonResponse
import json

# Create your views here.
def store(request):
    medicine = Medicine.objects.all()
    
    return render(request, 'medicine/store.html',{'medicine':medicine})

def about(request):
    return render(request, 'medicine/store.html')

def contact(request):
    return render(request, 'medicine/store.html')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print("username: ", username, " password: ", password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/', {'user':user})
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
        
    form = AuthenticationForm()
    return render(request, 'medicine/store.html', context={"form":form})

def register(request):
    if request.method == 'POST':
        password2 = request.POST['password2']
        form = RetailForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']              
            if password == password2:  
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username Taken')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'email already exist')
                    return redirect('MedicineTrack:register')
                else:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    user1 = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('/', {'user':user1})
                    else:
                        return redirect('MedicineTrack:login')
            else:
                messages.info(request,'password not match')
                return redirect('MedicineTrack:register')
    else:
        form = RetailForm()
    return render(request, 'medicine/store.html', context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    cache.clear()
    return redirect("MedicineTrack:store")


def order_medicine(request):
    return render(request, 'medicine/order_medcine.html')


def statistics(request):
    if request.user.is_authenticated:
        medicine = Medicine.objects.all()
        return render(request,'medicine/statistics.html',{'medicine':medicine})
    else:
        return redirect("MedicineTrack:store")
    
    
def order(request):
    return render(request, 'medicine/order.html')

def cart(request):
    if request.user.is_authenticated:
        retail = request.user.retail
        order, created = Order.objects.get_or_create(retail_id = retail, status=True)
        items = order.ordermedicine_set.all()
        medicinePrice = items
        print(dir(medicinePrice))
        cartMedicine = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartMedicine = order['get_cart_items']
        
    context = {'items':items,'order':order, 'cartMedicine':cartMedicine}
    return render(request, 'medicine/carts.html', context)

def checkout(request):
    if request.user.is_authenticated:
        retail = request.user.retail
        order, created = Order.objects.get_or_create(retail_id = retail, status=True)
        items = order.ordermedicine_set.all()
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
    context = {'items':items,'order':order}
    return render(request,'medicine/checkout.html',context)


def updateItem(request):
    data = json.loads(request.body)
    medicineId = data['medicineId']
    action = data['action']
    print('Action:', action)
    print('medicine:', medicineId)

    retail = request.user.retail
    medicine = Medicine.objects.get(id=medicineId)
    order, created = Order.objects.get_or_create(retail_id=retail, status=True)
    print(medicine)
    orderMedicine, created = OrderMedicine.objects.get_or_create(order_id=order, medicine_id=medicine)

    if action == 'add':
        orderMedicine.quantity = (orderMedicine.quantity + 1)
    elif action == 'remove':
        orderMedicine.quantity = (orderMedicine.quantity - 1)

    orderMedicine.save()

    if orderMedicine.quantity <= 0:
        orderMedicine.delete()

    return JsonResponse('Item was added', safe=False)
>>>>>>> d1e1965d5bdc091eef12f3c04bbb69ae343684a9
