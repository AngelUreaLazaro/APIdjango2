from django.shortcuts import redirect, render
from rest_framework.views import APIView
from .models import Usuario
from .forms import RegistroForm
from django.contrib.auth import authenticate, login 
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags



# Create your views here.
class Home(APIView):
    template_name='index.html'
    def get(self,request):
        return render(request,self.template_name)
class Registro(APIView):
    template_registro='registro.html'    
    def get(self,request):
        return render(request,self.template_registro)
class Login(APIView):
    template_login='login.html'
    def get(self,request):
        return render(request,self.template_login)
class Catalogo(APIView):
    template_catalogo='catalogo.html'
    def get(self,request):
        return render(request,self.template_catalogo)


class ProcesarRegistroView(APIView):
    template_name = 'registro.html'

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Componer el mensaje de correo electrónico
            subject = 'Confirmación de Registro'
            message = '¡Gracias por registrarte en nuestro sitio web! Tus detalles de registro son:'
            message += f'\nNombre: {user.nombre}'
            message += f'\nCorreo electrónico: {user.email}'
            # Puedes agregar otros detalles de registro aquí

            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]  # Usar el correo proporcionado por el usuario

            # Enviar el correo electrónico
            send_mail(
                subject, message, from_email, recipient_list,
                fail_silently=False,
            )

            return redirect('login')

        return render(request, self.template_name, {'form': form})



class LoginView(APIView):
    template_name = 'login.html'  # Reemplaza 'login.html' con el nombre de tu plantilla de inicio de sesión

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        usuario = request.POST.get('user')
        contrasena = request.POST.get('password')

        # Consulta la base de datos para encontrar un usuario con los datos ingresados
        try:
            user = Usuario.objects.get(usuario=usuario, contrasena=contrasena)
        except Usuario.DoesNotExist:
            user = None

        if user is not None:
            # Las credenciales son válidas
            # Realiza las acciones necesarias aquí
            return redirect('catalogo')  # Cambia 'catalogo' al nombre de tu página de destino
        else:
            # Las credenciales son incorrectas
            # Realiza las acciones necesarias aquí
            print(f'Valor de usuario: {usuario}')
            print(f'Valor de contraseña: {contrasena}')
            return render(request, self.template_name, {'error_message': 'Credenciales incorrectas'})
        