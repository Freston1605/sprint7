from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from .forms import RegistrationForm, CustomLoginForm, TareaForm
from .models import Tarea

from django.contrib import admin

# Create your views here.


# clase para visualizacion en panel Admin de Django
class TareaAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "descripcion",
        "fecha_vencimiento",
        "estado",
        "etiqueta",
        "urgencia",
        "responsable",
        "creado_por",
    )
    list_filter = ("estado", "etiqueta", "urgencia", "responsable", "creado_por")
    search_fields = (
        "titulo",
        "descripcion",
        "responsable__username",
        "creado_por__username",
    )
    ordering = ("-fecha_vencimiento",)


# muestra de landing
def landing_page(request):
    return render(request, "landing_page.html")


# Registro de usuarios
def register(request):
    """
    Función para registrar nuevos usuarios.
    La validación está hecha por los métodos de la clase RegistrationForm que hereda
    de AuthenticationForm
    """
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Guardar el nuevo usuario en la base de datos
            form.save()
            # Iniciar sesión automáticamente con el nuevo usuario
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir al usuario a una página después del registro exitoso
                return redirect("welcome")
    else:
        form = RegistrationForm()

    return render(request, "registration/register.html", {"form": form})


""" class RegistroUsuarioView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
 """


# Inicio de sesión
class CustomLoginView(LoginView):
    """
    Vista personalizada para manejar el inicio de sesiones. Hereda de LoginView.
    Redireige a welcome.html, tiene a login.html como plantilla y usa un el formulario
    CustomLoginForm.
    """

    authentication_form = CustomLoginForm
    next_page = "welcome"
    redirect_authenticated_user = True

    def form_invalid(self, form):
        """
        Método para manejar el caso de inicio de sesión inválido.
        Aquí puedes personalizar la forma en que se muestran los errores al usuario.
        """
        messages.error(
            self.request, "Inicio de sesión inválido. Verifica tus credenciales."
        )
        return super().form_invalid(form)


# Bienvenida después del inicio de sesión
@login_required
def welcome(request):
    return render(request, "welcome.html")


# Cierre de sesión
def logout_view(request):
    logout(request)
    return redirect("landing")


# Creación de tareas, los decoradores no funcionan con la clases
class CrearTareaView(CreateView):
    """
    Clase para crear una vista personalizada que sirva como base para crear
    tareas con el formulario TareaForm a partir del modelo Tarea.
    La clase hereda de CreateView y modifica los parámetros: model, template_name, form_class y
    success_url para adaptarse a las necesidades de la página.
    """

    model = Tarea
    template_name = "tareas/crear.html"
    form_class = TareaForm

    def form_valid(self, form):
        """
        Método heredado que permite la validación de los datos del formulario
        La funcionalidad añadida es que automáticamente asigna
        al campo 'creado_por' al usuario que inició sesión.
        """
        form.instance.creado_por = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Método heredado para manejar el caso de formulario inválido.
        La funcionalidad añadida es que se muestren en la página a
        través de clases de django todos los errores captados por django.
        """
        for field in form:
            for error in field.errors:
                messages.error(self.request, f"{field.label} - {error}")
        return super().form_invalid(form)

    def get_success_url(self):
        """
        Método para obtener la URL de redirección después de que el formulario es válido.
        """
        messages.success(
            self.request, "¡Tarea creada exitosamente!"
        )  # Agregar mensaje de éxito
        return reverse(
            "tareas_pendientes"
        )  # Utilizar la función reverse en lugar de reverse_lazy


# modificacion de lsta de tareas para que muestre las completas y las pendientes separado

def tareas_pendientes(request):
    tareas_pendientes = Tarea.objects.exclude(estado="completada")
    return render(request,"tareas/pendientes.html", {"tareas_pendientes": tareas_pendientes})

def tareas_completadas(request):
    tareas_completadas = Tarea.objects.filter(estado="completada")
    return render(request, 'tareas/completadas.html', {"tareas_completadas": tareas_completadas})

# funcion para completar las tareas
def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    if request.method == "POST":
        tarea.estado = "completada"
        tarea.save()
        messages.success(request, "La tarea ha sido completada exitosamente.")
        return redirect("tareas_pendientes")
    # Redireccion a pagina lista
    return render(request, "tareas/pendientes.html", {"tarea": tarea})


# funcion para cambio de prioridad
def cambiar_prioridad(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    if request.method == "POST":
        urgencia = request.POST.get("urgencia")
        tarea.urgencia = urgencia
        tarea.save()

        # Redireccion a pagina lista
        return redirect("tareas_pendientes")

    return render(request, "tareas/pendientes.html", {"tarea": tarea})

def ver_detalles(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    detalles_html = f"""
                <div class="table-responsive">
                    <table class="table table-primary mb-0">
                        <thead>
                            <tr>
                                <th scope="col">Título</th>
                                <th scope="col">Descripción</th>
                                <th scope="col">Fecha de Vencimiento</th>
                                <th scope="col">Estado</th>
                                <th scope="col">Urgencia</th>
                                <th scope="col">Asignado a</th>
                                <th scope="col">Creado por</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td scope="row">{tarea.titulo}</td>
                                <td>{tarea.descripcion}</td>
                                <td>{tarea.fecha_vencimiento}</td>
                                <td>{tarea.estado}</td>
                                <td>{tarea.urgencia}</td>
                                <td>{tarea.responsable}</td>
                                <td>{tarea.creado_por}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
           
    """
    return HttpResponse(detalles_html)