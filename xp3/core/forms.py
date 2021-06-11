from django import forms
from django.forms import ModelForm 
from .models import Vehiculo

class VehiculoForm(ModelForm):
    
    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'categoria',]