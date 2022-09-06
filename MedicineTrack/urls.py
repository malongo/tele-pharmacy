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
    path('edit-profile', views.updateProfile, name="update_profile"),
    path('medicine/<str:pk>', views.medicine_info, name="medicine-info"),
    path('process/<str:pk>', views.order_process, name="order_process"),
    path('payment/<str:pk>', views.payment, name="payment"),
    path('get_data', views.get_data, name="get-data"),
    path('delete-order/<str:pk>', views.delete_order, name="delete-order"),
    path('edit-order/<str:pk>', views.edit_order, name="edit-order"),
    path('message/<str:pk>', views.message, name="message"),
    path('user-profile', views.user_profile, name="profile"),
]