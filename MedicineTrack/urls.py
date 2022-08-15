from django.urls import path
from . import views

urlpatterns = [
    path('Retaildetails', views.RetailDetails, name="RetailDetails"),
    path('addretail', views.addRetail, name="addRetail"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    # path('about', views.about, name="about"),
    
]