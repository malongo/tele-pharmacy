from django.contrib import admin
from .models import Status,OrderStatus,Medicine,Retail,OrderMedicine,Order,MedicinePrice,Shipping

# Register your models here.
admin.site.register([Status,OrderStatus,Medicine,Retail,OrderMedicine,Order,MedicinePrice,Shipping])

