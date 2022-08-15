from django.contrib import admin
from .models import Retail,Order,Shipping
# Register your models here.

admin.site.register([Retail,Order,Shipping])