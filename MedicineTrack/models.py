from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User 
import random
# Create your models here.

class Status(models.Model):
    status_name = models.CharField(default = True, unique = True, max_length = 100)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.status_name

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.name)
    
    @property
    def imageURL(self):
        medicine_photo = self.medicinephoto_set.all()
        for photo in medicine_photo:
            #random.randrange(1,4,1)
            try:
                url = photo.photo.url
            except:
                url = ''
            return url
    
    @property
    def getPrice(self):
        medicinePrice = MedicinePrice.objects.get(medicine_id=self)
        return medicinePrice.price

class MedicinePrice(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete = models.CASCADE)
    price = models.FloatField()
    status = models.BooleanField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def __str__(self):
        return self.medicine.name + ": " + str(self.price) + "$"
    
    
class MedicinePhoto(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete = models.CASCADE)
    photo =  models.ImageField("Medicine photo",upload_to = 'pics/', null = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
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
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    PhoneNumber_1 = models.CharField(max_length = 15, null=True) 
    PhoneNumber_2 = models.CharField(max_length = 15, null = True)
    Country = CountryField(null=False)
    City = models.CharField(max_length = 3, choices = CITIES,)
    Address = models.CharField(max_length = 254,)
    RetailEmail = models.EmailField(max_length = 254,)
    OrganizationName = models.CharField(max_length = 254)
    status = models.BooleanField(default = True)

    def __str__ (self):
        return self.user.username 
        
class Order(models.Model):
    retail = models.ForeignKey(Retail,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.BooleanField(default=False)
    complete = models.BooleanField(default=False) #allow to see if order complete or not
    
    def __str__(self):
        return str(self.id) + " by " + str(self.retail) + ''
    
#addition functions
    @property
    def shipping(self):
        shipping = False
        orderitems = self.ordermedicine_set.all()
        for i in orderitems:
            if i.medicine == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.ordermedicine_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = OrderMedicine.objects.filter(order__id = self.id)
        total = sum([item.quantity for item in orderitems])
        # total = orderitems.count()
        return total 
    
    @property
    def get_status(self):
        order_status = Status.objects.get(orderstatus__order__id = self.id)
        print(order_status)
        return order_status.status_name
       
       
class OrderStatus(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE) 
    status_name = models.ForeignKey(Status, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    status_date = models.DateTimeField(auto_now_add=True)
    
class OrderMedicine(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    medicine = models.ForeignKey(Medicine,  on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    total_price = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
      
    def __str__(self):
        return str(self.order) + " " + str(self.medicine)
    
    @property
    def get_total(self):
        total = self.medicine.getPrice * self.quantity
        return total
class ShippingAddress(models.Model):
    retail = models.ForeignKey(Retail, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
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

class Contact(models.Model):
    name=models.CharField(max_length=254,null=False)
    email=models.EmailField(null=False)
    subject=models.TextField(null=False)