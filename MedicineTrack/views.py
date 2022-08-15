from django.shortcuts import render,redirect
from .models import Shipping
from .forms import FormShipping

# Create your views here.
ship=Shipping.objects.all()
#ord=Retail.objects.get(retail_id)


def index(request):
    return render(request, 'medicine/index.html')

def details(request):
    return render(request,'shippdetails.html',{'Shipping':ship})
def shipping(request): 
    if request.method == 'POST':
        form=FormShipping(request.POST or None,request.FILES)
        if form.is_valid():

         form.save()
         return redirect('MedicineTrack:details')
    else:
        form = FormShipping()
    return render(request,'shipping.html',{'form':form})

