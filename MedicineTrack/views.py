from django.shortcuts import render
from .models import OrderMedicine,OrderStatus
# Create your views here.
def index(request):
    return render(request, 'medicine/index.html')
def show(request):
    showm = OrderMedicine.objects.all()
    return render(request,'showorder.html',{'showm':showm})
