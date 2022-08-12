from django.db import models

# Create your models here.
class Orders(models.Model):
    retail_id=models.ForeignKey(Retail,on_delete=CASCADE)
    order_date=models.DateTimeField()
    status=models.BooleanField(default=True)

    def_str_(self):
    return self.retail_id:

    class Status(models.Model):
        status_name=models.CharField(default=True)
        status=models.BooleanField()



