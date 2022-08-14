from django.shortcuts import render
from .models import Shipping
from .forms import FormShipping

# Create your views here.
ship=Shipping.objects.all()

def index(request):
    return render(request, 'base.html')
def shipping(request): 
    if request.method == 'POST':
        form=FormShipping(request.POST or None,request.FILES)
        if form.is_valid():

         form.save()
         #return redirect('baraka:famm')
    else:
        form = FormShipping()
    return render(request,'shipping.html',{'form':form})