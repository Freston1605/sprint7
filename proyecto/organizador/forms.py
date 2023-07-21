from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Tarea


class RegistrationForm(UserCreationForm):
    """
    Formulario con los campos necesarios para crear un nuevo usuario.
    Hereda de UserCreationForm y utiliza User como modelo base.
    Los campos tienen etiquetas personalizadas para ser mostradas en español correctamente en la página.
    Está hecho para que pueda funcionar con un iterable de django con la finalidad
    de automatizar la implementación el formulario con bootstrap.
    """

    # Hereda la validación del formulario de UserCreationForm
    # Para eso se implementa password1 y password2
    # Pero sólo se modifican para mostrar correctamente la etiqueta con bootstrap y ofuscar la casilla de la contraseña
    username = forms.CharField(label="Nombre de usuario")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class CustomLoginForm(AuthenticationForm):
    """
    Formulario para iniciar sesión que modifica a AuthenticationForm para
    tener los nombres de las etiquetas en español en la página de inicio.
    Está hecho para que pueda funcionar con un iterable de django con la finalidad
    de automatizar la implementación el formulario con bootstrap.
    """

    # Asignando las etiquetas y el widget de Contraseña para proteger los caracteres ingresados.
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label=("Contraseña"), widget=forms.PasswordInput)


class TareaForm(forms.ModelForm):

    """
    Formulario para las tareas a partir del modelo 'Tarea'.
    Está hecho para que pueda funcionar con un iterable de django con la finalidad
    de automatizar la implementación el formulario con bootstrap.
    """

    ESTADOS = (
        ("pendiente", "Pendiente"),
        ("en_progreso", "En Progreso"),
        ("completada", "Completada"),
    )

    etiquetas_choices = (
        ("trabajo", "Trabajo"),
        ("hogar", "Hogar"),
        ("estudio", "Estudio"),
    )
    # Asignando a cada campo la las selecciones, la etiqueta y la clase para que pueda ser mostrado por bootstrap
    estado = forms.ChoiceField(
        choices=ESTADOS,
        label="Estado",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    etiqueta = forms.ChoiceField(
        choices=etiquetas_choices,
        label="Etiqueta",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    responsable = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Asignar a",
        empty_label="Seleccione un usuario",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    fecha_vencimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Tarea
        fields = [
            "responsable",
            "titulo",
            "descripcion",
            "fecha_vencimiento",
            "estado",
            "etiqueta",
        ]