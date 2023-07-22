from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('accounts/registration/', views.register, name='registration'),
    path('accounts/login', views.CustomLoginView.as_view(), name='login'),
    path('accounts/logout', views.logout_view, name='logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('tarea/crear/', views.CrearTareaView.as_view(), name="crear_tarea"),
    path('tarea/completadas/', views.tareas_completadas, name='tareas_completadas'),
    path('detalles_tarea/<int:tarea_id>/', views.ver_detalles, name='detalles_tarea'),
    path('tarea/<int:tarea_id>/completar/', views.completar_tarea, name='completar_tarea'),
    path('tarea/<int:tarea_id>/cambiar_prioridad/', views.cambiar_prioridad, name='cambiar_prioridad'),
    path('tareas/pendientes/', views.tareas_pendientes, name='tareas_pendientes')
]
