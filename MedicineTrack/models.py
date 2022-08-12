from django.db import models

# Create your models here.
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

        



       


 