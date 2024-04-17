from django import forms
from .models import Clase1, Clase2, Clase3

class Clase1Form(forms.ModelForm):
    class Meta:
        model = Clase1
        fields = ['campo1', 'campo2']

class Clase2Form(forms.ModelForm):
    class Meta:
        model = Clase2
        fields = ['campo3', 'campo4']

class Clase3Form(forms.ModelForm):
    class Meta:
        model = Clase3
        fields = ['campo5', 'campo6']

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100)