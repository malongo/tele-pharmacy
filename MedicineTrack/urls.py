from django.urls import path
from . import views

app_name = "MedicineTrack"

urlpatterns = [
   
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('', views.medicine_store, name='store'),
    path('login', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('about', views.about, name='about'),
    path('statistics', views.statistics, name='statistics'), 
    path('order', views.order, name='order'), 
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('profile', views.updateProfile, name="update_profile"),
    path('medicine/<str:pk>', views.medicine_info, name="medicine-info"),
]