from .models import OrderMedicine
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect,JsonResponse
from MedicineTrack.models import Retail,Contact
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db.models import Q
import json
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MedicineSerializer

# Create your views here.

@api_view(['GET'])
def getMedicine(request):
    best_sell = OrderMedicine.objects.filter(order__id__gte = 1).order_by("-quantity")[:6]
    serializer = MedicineSerializer(best_sell, many=True)
    return Response(serializer.data)


def medicine_store(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    medicine = Medicine.objects.filter(
            Q(name__icontains = q) |
            Q(description__icontains = q) 
        )
    best_sell = OrderMedicine.objects.filter(order__id__gte = 1).order_by("-quantity")[:6]
    feature_product = MedicinePrice.objects.all().order_by('price')
    context = {'best_sell':best_sell,'medicine':medicine,'feature_product':feature_product}
    return render(request, 'medicine/main.html',context)

def about(request):
    return render(request, 'medicine/about.html')

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
                    messages.success(request, f"You are now logged in as {username}")
                    return redirect('/admin')
                else:
                    messages.success(request, f"You are now logged in as {username}")
                    return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
        
    form = AuthenticationForm()
    return render(request, 'medicine/login_register.html', context={"form":form})


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
                l, u, p, d = 0, 0, 0, 0
                s = password
                if (len(s) >= 8):
                    for i in s:

                        # counting lowercase alphabets
                        if (i.islower()):
                            l+=1		

                        # counting uppercase alphabets
                        if (i.isupper()):
                            u+=1		

                        # counting digits
                        if (i.isdigit()):
                            d+=1		

                        # counting the mentioned special characters
                        if(i=='@'or i=='$' or i=='_'):
                            p+=1		
                if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
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
                    messages.warning(request,'Weak Password')
                    return redirect('MedicineTrack:register')

            else:
                messages.info(request,'password not match')
                return redirect('MedicineTrack:register')
    else:
        form = RetailForm()
    return render(request, 'medicine/login_register.html', context={"form":form})


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
    if request.user.is_authenticated and not request.user.is_superuser:
        order = Order.objects.filter(retail=request.user.retail)
    
    else:
        order = []
    return render(request, 'medicine/order.html',{'order':order})

#already modified
def cart(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        retail = request.user.retail
        status = Status.objects.get(status_name = "Not submitted")
        try:
             order, created = Order.objects.get_or_create(retail = retail, complete=False,)
        except Order.MultipleObjectsReturned:
            #raise Http404("Your can't process to order at once remove one and continue") 
            order = Order.objects.filter(retail = retail, complete=False).first()
        items = order.ordermedicine_set.all()
        
        print(order)
   
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        
    context = {'items':items,'order':order}
    return render(request, 'medicine/carts.html', context)

def checkout(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        retail = request.user.retail
        try:
            order, created = Order.objects.get_or_create(retail = retail, complete=False)
        except Order.MultipleObjectsReturned:
            order = Order.objects.filter(retail = retail, complete=False).first()
        items = order.ordermedicine_set.all()
        if request.method == 'POST':
            form=FormShipping(request.POST or None,request.FILES,instance =  retail)
            if form.is_valid():
                form.save()
                return redirect('MedicineTrack:details')
            
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
    form = FormShipping(instance = request.user.retail)
    context = {'items':items,'order':order,'form':form,}
    return render(request,'medicine/checkout.html',context)


def updateItem(request):
    data = json.loads(request.body)
    medicineId = data['medicineId']
    action = data['action']
    medicineQt= data['medicineQt']
    # medicineQuantity = data['medicineQuantity']
    print("medicine: ",medicineId)
    print("action: ",action)
    print("medicineQuantity: ",medicineQt)
    retail = request.user.retail
    medicine = Medicine.objects.get(id=medicineId)
    try:
        order, created = Order.objects.get_or_create(retail = retail, complete=False)
    except Order.MultipleObjectsReturned:
        order = Order.objects.filter(retail = retail, complete=False).first()
    
    orderMedicine, created = OrderMedicine.objects.get_or_create(order=order, medicine=medicine)

    if action == 'add':
        orderMedicine.quantity = (orderMedicine.quantity + medicineQt)
        messages.info(request,f"Your successful adding {medicineQt} {orderMedicine.medicine.name}")
    elif action == 'remove':
        orderMedicine.quantity = (orderMedicine.quantity - medicineQt)
        messages.info(request,f"Your successful remove {medicineQt} {orderMedicine.medicine.name}")
    elif action == 'addCart':
        orderMedicine.quantity = (orderMedicine.quantity + medicineQt)
        messages.info(request,f"Your successful adding {medicineQt} {orderMedicine.medicine.name}")
    elif action == 'removeCart':
        orderMedicine.quantity = (orderMedicine.quantity - medicineQt)
        messages.info(request,f"Your successful remove {medicineQt} {orderMedicine.medicine.name}")
    elif action == 'removeAll':
        orderMedicine.quantity = 0
        messages.info(request,f"Your successful remove all {orderMedicine.medicine.name} ")
    orderMedicine.save()

    if orderMedicine.quantity <= 0:
        orderMedicine.delete()

    return JsonResponse('Item was added ', safe=False)



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

def payment(request,pk):
    order = Order.objects.get(pk=pk)
    items = order.ordermedicine_set.all()
    status = Status.objects.all()
    for status in status:
        if status.status_name == 'wait for payment':
            status.status = True
            order.order_status = status
            order.complete = True
            order.save()
        else:
            status.status = False
            status.save()
    return render(request, 'medicine/payment.html',{'order':order,'items':items })

def order_process(request,pk):
   
    
    return redirect('MedicineTrack:payment')




def delete_order(request,pk):
    order = Order.objects.get(id=pk)
   
    if request.user != order.retail.user:
        return HttpResponse("your not allowed here!!!")
    
    if request.method == 'POST':
        order.delete()
        return redirect('MedicineTrack:order')
    return render(request,'medicine/delete-order.html',{'obj':order})

def edit_order(request,pk):
    order = Order.objects.get(pk=pk)
    # items = order.ordermedicine_set.all()
    status = Status.objects.all()
    for status in status:
        if status.status_name == 'Not submitted':
            status.status = True
            order.order_status = status
            order.complete = False
            order.save()
        else:
            status.status = False
            status.save()
            
    return redirect('MedicineTrack:order')
    
def message(request,message):
    
    return render(request, 'medicine/message.html',{'message':message})


def user_profile(request):
    return render(request,'medicine/profile.html')


def browse(request):
    q = request.GET.get('q').upper() if request.GET.get('q') != None else ''
    medicine = Medicine.objects.filter(
            Q(name__startswith = q) 
           
        ).order_by('name')
    context = {'medicine':medicine}
    return render(request,'medicine/browse_medicine.html',context)
    

def browse_medicine(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    medicine = Medicine.objects.filter(
            Q(name__icontains = q) |
            Q(description__icontains = q)  
           
        )
    context = {'medicine':medicine}
    return render(request,'medicine/browse_medicine.html',context)


def product(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    medicine = Medicine.objects.filter(
            Q(name__icontains = q) |
            Q(description__icontains = q)  
           
        )
    context = {'medicine':medicine}
    return render(request,'medicine/product.html',context)




def shopping(request,pk):
    medicine = Medicine.objects.get(pk=pk)
    medicine_photo = MedicinePhoto.objects.filter(medicine__name = medicine.name)
    form = AuthenticationForm()
    context = {'medicine':medicine,'medicine_photo':medicine_photo,'form':form}
    
    return render(request,'medicine/shopping.html',context)

