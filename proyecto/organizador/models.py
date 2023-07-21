from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tarea(models.Model):
    """
    Clase para el modelo de Tareas.
    Tiene como atributos: quien creó la tarea 'creado_por'
    (asignado automáticamente al usuario que hizo inicio de sesión),
    responsable (a quién va dirigida la tarea), estado (de la tarea),
    etiqueta (de la tarea), fecha de vencimiento y una descripción.
    """

    # Elecciones para estado, etiqueta y urgencia
    ESTADOS_CHOICES = (
        ("pendiente", "Pendiente"),
        ("en_progreso", "En Progreso"),
        ("completada", "Completada"),
    )

    ETIQUETAS_CHOICES = (
        ("trabajo", "Trabajo"),
        ("hogar", "Hogar"),
        ("estudio", "Estudio"),
    )

    URGENCIA_CHOICES = (
        ("alta", "Alta"),
        ("media", "Media"),
        ("baja", "Baja"),
    )

    # Atributos
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateField()
    # Atributos con elección de una lista
    estado = models.CharField(
        max_length=20, 
        choices=ESTADOS_CHOICES, 
        default="pendiente"
    )
    etiqueta = models.CharField(
        max_length=20, 
        choices=ETIQUETAS_CHOICES, 
        default='trabajo'
    )
    urgencia = models.CharField(
        max_length=10, 
        choices=URGENCIA_CHOICES, 
        default="baja"
    )
    # Este campo es automáticamente asignado en la vista al usuario autenticado
    creado_por = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name="tareas_creadas"
    )
    responsable = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tareas_asignadas",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.titulo
