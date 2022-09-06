from django.contrib import admin
from .models import *

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    #fields = ['retail', 'order_date','order_status','complete']
    list_display = ('retail','order_date','order_status','complete',)
    
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name','photo','status')
class MedicinePriceAdmin(admin.ModelAdmin):
    list_display = ('medicine_id','price','status','start_date','end_date')
class OrderMedicineAdmin(admin.ModelAdmin):
    list_display = ('order','medicine','quantity')
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_name','status')
class RetailAdmin(admin.ModelAdmin):
    list_display = ('user','PhoneNumber_1','PhoneNumber_2','Country','City','Address','RetailEmail','OrganizationName','Status')
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('retail','order','country','city','address','email','phone_number')
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject')
        
admin.site.register(Order, OrderAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(MedicinePrice, MedicinePriceAdmin)
admin.site.register(OrderMedicine, OrderMedicineAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Retail, RetailAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(Contact, ContactAdmin)
#admin.site.register([,Contact])

