from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('accounts/registration/', views.register, name='registration'),
    path('accounts/login', views.CustomLoginView.as_view(), name='login'),
    path('accounts/logout', views.logout_view, name='logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('crear_tarea/', views.CrearTareaView.as_view(), name="crear_tarea"),
    path('lista_tareas/', views.lista_tareas, name='lista_tareas'),
]
