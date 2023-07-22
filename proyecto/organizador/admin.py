from django.contrib import admin
from .models import Tarea
from .views import TareaAdmin
# Register your models here.

admin.site.site_header = 'Administración de Tareas'
admin.site.site_title = 'Tareas'
admin.site.index_title = 'Administrar Tareas'
admin.site.register(Tarea, TareaAdmin)