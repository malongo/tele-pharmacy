from .models import OrderMedicine,OrderStatus
from django.shortcuts import render, redirect
from django.http import HttpResponse
from MedicineTrack.models import Retail,Contact
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.cache import cache
from django.http import JsonResponse
import json

# Create your views here.

def medicine_store(request):
    medicine = Medicine.objects.all()
    if request.user.is_authenticated:
        retail = request.user.retail
        order, created = Order.objects.get_or_create(retail = retail, complete=False)
        cartMedicine = order.get_cart_items
   
    else:
        order = {'get_cart_items':0,'get_cart_total':0}
        cartMedicine = order['get_cart_items']
    
    
    return render(request, 'medicine/medicine-store.html',{'medicine':medicine,'cartMedicine':cartMedicine})

def about(request):
    if request.user.is_authenticated:
        retail = request.user.retail
        order, created = Order.objects.get_or_create(retail = retail, complete=False)
        items = order.ordermedicine_set.all()
        medicinePrice = items
        # print(dir(medicinePrice))
        cartMedicine = order.get_cart_items
   
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartMedicine = order['get_cart_items']
        
    return render(request, 'medicine/about.html',{'cartMedicine':cartMedicine})

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact = Contact(name=name, email=email, subject=subject)
        contact.save()
        return HttpResponse("<h1>Thanks for contact us</h1>")
    return render(request, 'medicine/contact.html')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #check if is super user
                if user.is_superuser:
                    return redirect('/admin')
                else:
                    messages.info(request, f"You are now logged in as {username}")
                    return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
        
    form = AuthenticationForm()
    return render(request, 'medicine/medicine-store.html', context={"form":form})


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
                    #create retail
                    Retail.objects.create(user = user, PhoneNumber_1 = '0629444617')
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('/')
                    else:
                        return redirect('MedicineTrack:login')
            else:
                messages.info(request,'password not match')
                return redirect('MedicineTrack:register')
    else:
        form = RetailForm()
    return render(request, 'medicine/medicine-store.html', context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    cache.clear()
    return redirect("MedicineTrack:store")


def order_medicine(request):
    return render(request, 'medicine/order_medcine.html')


def medicine_info(request,pk):
    medicine = Medicine.objects.filter(name=pk)
    return render(request,'medicine/medicine-info.html',{'medicine':medicine})


def statistics(request):
    if request.user.is_authenticated:
        medicine = Medicine.objects.all()
        return render(request,'medicine/statistics.html',{'medicine':medicine})
    else:
        return redirect("MedicineTrack:store")
    
    
def order(request):
    if request.user.is_authenticated:
        showOrder = Order.objects.filter(retail=request.user.retail)
    
    else:
        showOrder = []
    return render(request, 'medicine/order.html',{'showOrder':showOrder})

#already modified
def cart(request):
    if request.user.is_authenticated:
        retail = request.user.retail
        order, created = Order.objects.get_or_create(retail = retail, complete=False)
        items = order.ordermedicine_set.all()
        #added soon
        OrderStatus.objects.get_or_create(order=order, status_name =Status.objects.get(pk=1))
        medicinePrice = items
        # print(dir(medicinePrice))
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
        order, created = Order.objects.get_or_create(retail = retail, complete=False)
        items = order.ordermedicine_set.all()
        if request.method == 'POST':
            form=FormShipping(request.POST or None,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('MedicineTrack:details')
            
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
    form = FormShipping()
    context = {'items':items,'order':order,'form':form,}
    return render(request,'medicine/checkout.html',context)


def updateItem(request):
    data = json.loads(request.body)
    medicineId = data['medicineId']
    action = data['action']
    retail = request.user.retail
    medicine = Medicine.objects.get(id=medicineId)
    order, created = Order.objects.get_or_create(retail=retail, complete=False)
    orderMedicine, created = OrderMedicine.objects.get_or_create(order=order, medicine=medicine)

    if action == 'add':
        orderMedicine.quantity = (orderMedicine.quantity + 1)
    elif action == 'remove':
        orderMedicine.quantity = (orderMedicine.quantity - 1)

    orderMedicine.save()

    if orderMedicine.quantity <= 0:
        orderMedicine.delete()

    return JsonResponse('Item was added', safe=False)



def updateProfile(request):
    user = request.user.retail
    form = FormRetail(instance=user)
    
    if request.method == 'POST':
        form = FormRetail(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/', pk=user.id)
    context = {'form':form}
    return render(request, 'medicine/update-profile.html',context)

