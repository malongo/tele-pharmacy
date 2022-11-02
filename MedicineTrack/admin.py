from django.contrib import admin
from .models import *

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    #fields = ['retail', 'order_date','order_status','complete']
    list_display = ('retail','order_date','order_status','complete',)
    
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','status','updated_at')
class MedicinePriceAdmin(admin.ModelAdmin):
    list_display = ('medicine','price','status','start_date','end_date')
class OrderMedicineAdmin(admin.ModelAdmin):
    list_display = ('order','medicine','quantity')
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_name','status')
class RetailAdmin(admin.ModelAdmin):
    list_display = ('user','PhoneNumber_1','PhoneNumber_2','Country','City','Address','RetailEmail','OrganizationName','status')
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('retail','order','country','city','address','email','phone_number')
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject')
    
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('order','status_name','status','status_date')
    
class MedicinePhotoAdmin(admin.ModelAdmin):
    list_display = ('medicine','photo','created_date','updated_date')
        
admin.site.register(Order, OrderAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(MedicinePrice, MedicinePriceAdmin)
admin.site.register(OrderMedicine, OrderMedicineAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Retail, RetailAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(MedicinePhoto, MedicinePhotoAdmin)
#admin.site.register([,Contact])

