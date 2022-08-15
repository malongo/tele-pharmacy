from django import forms
from MedicineTrack.models import Retail
from .models import *

class FormRetail(forms.ModelForm):
    class Meta:
        model=Retail
        fields="__all__"