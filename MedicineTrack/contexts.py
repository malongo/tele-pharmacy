from .models import *
from django.shortcuts import render, redirect

def order_cart(request):
   
    try:
        new_medicine_item = Medicine.objects.filter().order_by('-created_at')[1:]
    except Medicine.DoesNotExist:
        new_medicine_item = None
        
    if new_medicine_item is not None:
        new_medicine = new_medicine_item
        
    else:
        new_medicine = {}
        recent_cart= {}
        
    if request.user.is_authenticated and not request.user.is_superuser:
        retail = request.user.retail
        try:
            order = Order.objects.get(retail = retail, complete=False)
        except Order.MultipleObjectsReturned:
            order = Order.objects.filter(retail = retail, complete=False).first()
        except Order.DoesNotExist:
            order = None
            
     
           
            
        if order is not None:
            cartMedicine = order.get_cart_items
            recent_cart = OrderMedicine.objects.filter(order = order)
            
        else:
            order = {'get_cart_items':0,'get_cart_total':0}
            cartMedicine = order['get_cart_items']
   
    else:
        order = {'get_cart_items':0,'get_cart_total':0}
        cartMedicine = order['get_cart_items']
        recent_cart= {}
        
   #'recent_cart':recent_cart,
    return {'cartMedicine': cartMedicine,'new_medicine':new_medicine}


def order_status(request):
    if request.user.is_authenticated:
        order = Order.objects.filter(retail = request.user)
    else:
        order = {}
    return {'order':order}