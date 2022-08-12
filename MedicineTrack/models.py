from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User 


# Create your models here.
class Orders(models.Model):
    retail_id=models.ForeignKey(Retail,on_delete=CASCADE)
    order_date=models.DateTimeField()
    status=models.BooleanField(default=True)
    def _str_(self):
      return self.retail_id:

class Status(models.Model):
        status_name=models.CharField(default=True)
        status=models.BooleanField()

class Medicine(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=400)
    photo=  models.ImageField("Medicine photo",upload_to = 'pics/',null=True)
    status=models.BooleanField(default=True)

class Retail(models.Model):
    CITIES = (
        ('Ars','Arusha')
        ('Bkb','Bukoba')
        ('Dsm','Dar es salaam')
        ('Mwz','Mwanza')
        ('Dom', 'Dodoma')
        ('klm','Kilimanjaro')
        ('Irg','Iringa')
        ('Njo','Njombe')
        ('Tng', 'Tanga')
        ('Mby','Mbeya')
        ('Mor','Morogoro')
        ('Sng','Singida')

    )
      user_id=models.OneToOneField(User, on_delete=models.CASCADE)
      PhoneNumber_1= models.CharField(max_length=15 required=True) 
      PhoneNumber_2= models.CharField(max_length=15, null=True)
      Country = CountryField(required=True)
      City = models.CharField(max_length=3, choices=CITIES, required=True)
      Address=models.CharField(max_length=254, required=True)
      RetailEmail=models.EmailField(max_length=254, required=True)
      OrganizationName=models.CharField(max_length=254)
      Status=models.BooleanField(default=True)

      def __str__ (self):
            return self.user_id.username 

class OrderStatus(models.Model):
       order_id=models.ForeignKey(Order,on_delete=CASCADE)
       status_name=models.CharField(max_length=100)
       Status=models.BooleanField(default=True)
       def __str__(self) -> str:
           return self.order_id
class OrderMedicine(models.Model):
      order_id=models.ForeignKey(Order,on_delete=CASCADE)
      medicine_id=models.OneToOneField(Medicine,on_delete=models.CASCADE)
      quantity=models.IntegerField()
      total_price=models.FloatField()
      
      def __str__(self) -> str:
            return self.medicine_id