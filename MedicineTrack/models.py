from django.db import models
from django_countries.fields import CountryField
# Create your models here.

class Shipping(models.Model):
    order_id=models.OneToOneField(Order,on_delete=models.CASCADE)
    country= CountryField(blank=True)
    CITIES=(
        ('DOM','DODOMA'),
        ('DSM','DAR-ES-SALAAM'),
        ('ARS','ARUSHA'),
        ('MBY','MBEYA'),
        ('KLM','KILIMANJARO'),
        ('BKB','BUKOBA'),
        ('IRI','IRINGA'),
        ('NJO','NJOMBE'),
    )
    city=models.CharField(max_length=3, choices=CITIES)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phonenumber=models.CharField(max_length=30)

