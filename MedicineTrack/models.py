from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User 
# Create your models here.

class Status(models.Model):
    status_name = models.CharField(default = True, unique = True, max_length = 100)
    status = models.BooleanField()

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    photo =  models.ImageField("Medicine photo",upload_to = 'pics/', null = True)
    status = models.BooleanField(default=True)
    
    
    def __str__(self):
        return str(self.description)
    
    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url
    
    @property
    def getPrice(self):
        medicinePrice = self.medicineprice_set.all()
        price = [item for item in medicinePrice]
        return price
    
    

class MedicinePrice(models.Model):
    medicine_id = models.ForeignKey(Medicine, on_delete = models.CASCADE)
    price = models.FloatField()
    status = models.BooleanField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def __str__(self):
        return self.medicine_id.name + ": " + str(self.price) + "$"

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
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False) #allow to see if order complete or not
    
    def _str_(self):
        return self.retail_id
    
#addition functions
    @property
    def shipping(self):
        shipping = False
        orderitems = self.ordermedicine_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.ordermedicine_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.ordermedicine_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 
  
class OrderStatus(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    status_name = models.CharField(max_length=100)
    Status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.order_id)
    
    
       
class OrderMedicine(models.Model):
    order_id = models.ForeignKey(Order, on_delete = models.CASCADE)
    medicine_id = models.OneToOneField(Medicine, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    total_price = models.FloatField(null=True)
      

    def __str__(self):
        return str(self.medicine_id)
    
    
    @property
    def get_total(self):
        #total = self.medicine_id.price * self.quantity
        return 45

        
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

class Contact(models.Model):
    name=models.CharField(max_length=254,null=False)
    email=models.EmailField(null=False)
    subject=models.TextField(null=False)