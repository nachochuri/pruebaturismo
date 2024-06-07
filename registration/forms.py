from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NewUserForm(UserCreationForm):

    email = forms.EmailField(required=True, help_text='Debe tener máximo 250 caracteres.')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        # Los campos aparecen en este orden en el formulario. No se debe modificar los widgets aquí
        # ya que se perdería toda la validación de Django
        

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Ya existe un usuario con este email, prueba con otro.')
        return email