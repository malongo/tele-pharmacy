from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Medicine, OrderMedicine

class MedicineSerializer(ModelSerializer):
    
    class Meta:
        model = OrderMedicine
        fields = '__all__'