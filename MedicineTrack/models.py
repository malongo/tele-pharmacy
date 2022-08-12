from django.db import models

# Create your models here.
class Medicine(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=400)
    photo=  models.ImageField("Medicine photo",upload_to = 'pics/',null=True
                             )
    status=models.BooleanField(default=True)