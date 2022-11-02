from dataclasses import field
from urllib import request
from django import forms
from django.contrib.auth.models import User
from .models import *

class user_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
class FormRetail(forms.ModelForm):
    class Meta:
        model=Retail
        fields="__all__"

class FormShipping(forms.ModelForm):
    retail = forms.ModelChoiceField(queryset=Retail.objects.filter(id=1))
    class Meta:
        model=ShippingAddress
        fields="__all__"
        exclude = ["order"]

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

