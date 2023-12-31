# Generated by Django 4.2.3 on 2023-07-21 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_progreso', 'En Progreso'), ('completada', 'Completada')], default='pendiente', max_length=20)),
                ('etiqueta', models.CharField(choices=[('trabajo', 'Trabajo'), ('hogar', 'Hogar'), ('estudio', 'Estudio')], max_length=20)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_vencimiento', models.DateField()),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas_creadas', to=settings.AUTH_USER_MODEL)),
                ('responsable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tareas_asignadas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
