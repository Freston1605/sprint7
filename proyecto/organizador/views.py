from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm, CustomLoginForm
# Create your views here.

def landing_page(request):
    return render(request, 'landing_page.html')

# Registro de usuarios
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Guardar el nuevo usuario en la base de datos
            form.save()
            # Iniciar sesión automáticamente con el nuevo usuario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir al usuario a una página después del registro exitoso
                return redirect('welcome')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

# Inicio de sesión
class CustomLoginView(LoginView):
    """
    Vista personalizada para manejar el inicio de sesiones. Hereda de LoginView.
    Redireige a welcome.html, tiene a login.html como plantilla y usa un el formulario
    CustomLoginForm.
    """
    authentication_form = CustomLoginForm
    next_page = "welcome.html"
    redirect_authenticated_user = True


    def form_invalid(self, form):
        """
        Método para manejar el caso de inicio de sesión inválido.
        Aquí puedes personalizar la forma en que se muestran los errores al usuario.
        """
        messages.error(self.request, "Inicio de sesión inválido. Verifica tus credenciales.")
        return super().form_invalid(form)
    
# Bienvenida después del inicio de sesión
@login_required
def welcome(request):
    return render(request, "welcome.html")

# Cierre de sesión
def logout_view(request):
    logout(request)
    return redirect("landing")
