from django.contrib import admin
<<<<<<< HEAD
from . models import Retail, Contact

# Register your models here.

admin.site.register([Retail,Contact])
=======
from .models import Status,OrderStatus,Medicine,Retail,OrderMedicine,Order,MedicinePrice,Shipping

# Register your models here.
admin.site.register([Status,OrderStatus,Medicine,Retail,OrderMedicine,Order,MedicinePrice,Shipping])
>>>>>>> d1e1965d5bdc091eef12f3c04bbb69ae343684a9
