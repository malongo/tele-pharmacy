from django.contrib import admin
# <<<<<<< HEAD
from . models import Contact

# Register your models here.

admin.site.register([Contact])
# =======
from .models import Status,OrderStatus,Medicine,Retail,OrderMedicine,Order,MedicinePrice,Shipping

# Register your models here.
admin.site.register([Status,OrderStatus,Medicine,Retail,OrderMedicine,Order,MedicinePrice,Shipping])
# >>>>>>> d1e1965d5bdc091eef12f3c04bbb69ae343684a9
