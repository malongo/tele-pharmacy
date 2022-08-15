from django.shortcuts import render,redirect
from django.http import HttpResponse
from MedicineTrack.models import Retail,Contact
from .forms import FormRetail
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'medicine/index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return HttpResponse("<h1>Thanks for contact us</h1>")
    return render(request, 'contact.html')

def RetailDetails(request):
    retaildetails = Retail.objects.all()
    return render(request,'retail.html',{'Retail':retaildetails})
       

def addRetail(request):
    if request.method == 'POST':
        form = FormRetail(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('RetailDetails')
    else:
        form = FormRetail()
    return render(request, 'addretail.html',{'form':form})


