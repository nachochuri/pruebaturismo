from django import forms
from .models import Complejo, Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

paises = [
    [0, 'Alemania'],
    [1, 'Argentina'],
    [2, 'Brasil'],
    [3, 'Chile'],
    [4, 'España'],
    [5, 'Italia'],
    [6, 'Uruguay']
]

class ExtendsUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('telefono', 'pais', 'avisos')