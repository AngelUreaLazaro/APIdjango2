from django.shortcuts import redirect, render
from rest_framework.views import APIView
from .models import Usuario
from .forms import RegistroForm
from django.contrib.auth import authenticate, login 
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import DatosCSV


# Create your views here.    
class Home(APIView):
    template_registro='index.html'    
    def get(self,request):
        return render(request,self.template_registro)
class Informes(APIView):
    template_registro='informes.html'    
    def get(self,request):
        return render(request,self.template_registro)
class Informacion(APIView):
    template_registro='informacion.html'    
    def get(self,request):
        return render(request,self.template_registro)
class Prueba(APIView):
    template_registro='prueba.html'    
    def get(self,request):
        return render(request,self.template_registro)
class Predial(APIView):
    template_registro='p_predial.html'    
    def get(self,request):
        return render(request,self.template_registro)
class Tianguis(APIView):
    template_registro='tianguis.html'    
    def get(self,request):
        return render(request,self.template_registro)
class Defuncion(APIView):
    template_registro='defuncion.html'    
    def get(self,request):
        return render(request,self.template_registro)
class General(APIView):
    template_registro='medica_general.html'    
    def get(self,request):
        return render(request,self.template_registro)