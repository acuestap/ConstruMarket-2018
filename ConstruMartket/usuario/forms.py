from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class FormularioUsuariosMasivo(forms.Form):
    total = forms.IntegerField(
        label='Total de usuarios (Min: 10 - Max: 500)',
        validators=[
            MinValueValidator(10),
            MaxValueValidator(500)
        ]
    )


class FormularioUsuarioBasico(forms.Form):
    #username = forms.CharField(label='Nombre de usuario', max_length=20,validators=[validate_username])
    username = forms.CharField(
        label='Nombre de usuario (Min: 5 - Max: 10) Caracteres',
        min_length=5,
        max_length=10)
    '''
    first_name = forms.CharField(label='Nombre', max_length=100)
    last_name = forms.CharField(label='Apellidos', max_length=100)
    email = forms.CharField(label='Correo', max_length=100)
    '''

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo',
        }