from django import forms
from datetime import datetime, date
from .models import Consulta

class DateInput(forms.DateInput):
    input_type = 'date'

class ConsultaForm(forms.ModelForm):

    fecha_ingreso = forms.DateField(widget=DateInput)
    fecha_salida = forms.DateField(widget=DateInput)
        
    class Meta:
        model = Consulta
        fields = ['mensaje','fecha_ingreso','fecha_salida', 'cantidad_mayores', 'cantidad_menores']
        widgets = {
            'mensaje': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escriba su consulta'}),
            'fecha_ingreso': forms.DateTimeField(),
            'fecha_salida': forms.DateTimeField(),
            'cantidad_mayores': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cantidad mayores'}),
            'cantidad_menores': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cantidad menores'})
        }
        labels = {
            'mensaje':'',
            'fecha_ingreso':'',
            'fecha_salida':'',
            'cantidad_mayores':'',
            'cantidad_menores':''
        }

