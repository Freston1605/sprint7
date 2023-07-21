from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    """
    Formulario con los campos necesarios para crear un nuevo usuario.
    Hereda de UserCreationForm y utiliza User como modelo base.
    Los campos tienen etiquetas personalizadas para ser mostradas en español correctamente en la página.
    """
    username = forms.CharField(label='Nombre de usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    """
    Formulario para iniciar sesión que modifica a AuthenticationForm para
    tener los nombres de las etiquetas en español en la página de inicio.
    """

    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label=("Contraseña"), widget=forms.PasswordInput)
