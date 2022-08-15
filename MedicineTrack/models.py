from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User 
# Create your models here.

class Status(models.Model):
    status_name = models.CharField(default = True, unique = True, max_length = 100)
    status = models.BooleanField()

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    photo =  models.ImageField("Medicine photo",upload_to = 'pics/', null = True)
    status = models.BooleanField(default=True)

class MedicinePrice(models.Model):
    medicine_id = models.ForeignKey(Medicine, on_delete = models.CASCADE)
    price = models.FloatField()
    status = models.BooleanField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Retail(models.Model):
    CITIES = (
        ('Ars','Arusha'),
        ('Bkb','Bukoba'),
        ('Dsm','Dar es salaam'),
        ('Mwz','Mwanza'),
        ('Dom', 'Dodoma'),
        ('klm','Kilimanjaro'),
        ('Irg','Iringa'),
        ('Njo','Njombe'),
        ('Tng', 'Tanga'),
        ('Mby','Mbeya'),
        ('Mor','Morogoro'),
        ('Sng','Singida'),

    )
    
    user_id = models.OneToOneField(User, on_delete = models.CASCADE)
    PhoneNumber_1 = models.CharField(max_length = 15,) 
    PhoneNumber_2 = models.CharField(max_length = 15, null = True)
    Country = CountryField(null=False)
    City = models.CharField(max_length = 3, choices = CITIES,)
    Address = models.CharField(max_length = 254,)
    RetailEmail = models.EmailField(max_length = 254,)
    OrganizationName = models.CharField(max_length = 254)
    Status = models.BooleanField(default = True)

    def __str__ (self):
        return self.user_id.username 
        
class Order(models.Model):
    retail_id = models.ForeignKey(Retail,on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    status = models.BooleanField(default=True)
    def _str_(self):
        return self.retail_id
  
class OrderStatus(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    status_name = models.CharField(max_length=100)
    Status = models.BooleanField(default=True)
    
       
class OrderMedicine(models.Model):
    order_id = models.ForeignKey(Order, on_delete = models.CASCADE)
    medicine_id = models.OneToOneField(Medicine, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
      
    
        
class Shipping(models.Model):
    order_id = models.OneToOneField(Order, on_delete = models.CASCADE)
    country = CountryField(blank = True)
    CITIES = (
        ('DOM','DODOMA'),
        ('DSM','DAR-ES-SALAAM'),
        ('ARS','ARUSHA'),
        ('MBY','MBEYA'),
        ('KLM','KILIMANJARO'),
        ('BKB','BUKOBA'),
        ('IRI','IRINGA'),
        ('NJO','NJOMBE'),
    )
    city = models.CharField(max_length=3, choices=CITIES)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=30)

