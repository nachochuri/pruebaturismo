from django.forms import BaseModelForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django import forms


# Create your views here.
class SignUpView(CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registro.html'

    def get_form(self):
        form = super(SignUpView, self).get_form()
        form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'})
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repita su contraseña'})

        return form