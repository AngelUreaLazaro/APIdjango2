from django.shortcuts import redirect, render
from rest_framework.views import APIView
from .models import Usuario
from .forms import RegistroForm
from .utils import enviar_correo_registro 

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
class ProcesarRegistroView(APIView):
    template_name = 'registro.html'  # Nombre de la plantilla HTML

    def get(self, request):
        form = RegistroForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el usuario en la base de datos
            enviar_correo_registro(form.cleaned_data['email'])
            return redirect('login')  # Redirige a la página de inicio de sesión

        return render(request, self.template_name, {'form': form})