from django import forms
<<<<<<< HEAD
from MedicineTrack.models import Retail
from .models import *

class FormRetail(forms.ModelForm):
    class Meta:
        model=Retail
        fields="__all__"
=======
from django.contrib.auth.models import User
from django.db.models import fields

#forms here
class DateInput(forms.DateInput):
    input_type ='password'

class RetailForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'joeschmoe', 'name': 'username'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'joeschmoe@xyz.com', 'name': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'name': 'password'}))
    password2 = forms.CharField(label = "Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control',  'name': 'password2'}))

    
    class Meta:
        model = User
        fields = ['username', 'email', 'password','password2']
        # widgets = {"birthDate":DateInput(),}
        help_texts = {
            'username': None,
        }

>>>>>>> d1e1965d5bdc091eef12f3c04bbb69ae343684a9
