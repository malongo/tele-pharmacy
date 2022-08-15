from django.contrib import admin
from . models import Retail, Contact

# Register your models here.

admin.site.register([Retail,Contact])