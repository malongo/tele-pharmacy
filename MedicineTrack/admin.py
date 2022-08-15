from django.contrib import admin
from .models import OrderMedicine,OrderStatus,Medicine,Order,Retail
# Register your models here.
admin.site.register([OrderMedicine,OrderStatus,Medicine,Order,Retail])