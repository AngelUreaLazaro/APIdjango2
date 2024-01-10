"""API9ISC22 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import Home
from api.views import Registro
from api.views import Login
from api.views import ProcesarRegistroView
from api.views import LoginView
from api.views import Catalogo
from api.views import Arduinouno
from api.views import Arduinomega
from api.views import Protoboard
from api.views import Sensor
from api.views import PIC
from api.views import arduino_uno_details
from api.views import ComponentDetailView
from api.views import SendEmailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name='index'),
    path('registro.html', Registro.as_view(), name='registro'),
    path('login.html',Login.as_view(),name='login'),
    path('catalogo.html',Catalogo.as_view(),name='catalogo'),
    path('procesar_registro/', ProcesarRegistroView.as_view(), name='procesar_registro'),
    path('login/', LoginView.as_view(), name='loginview'),
    path('arduino-uno/', arduino_uno_details, name='arduino_uno_details'),
    path('arduino-uno.html/', Arduinouno.as_view(), name='arduinouno'),
    path('arduino-mega.html/', Arduinomega.as_view(), name='arduinomega'),
    path('protoboard.html/', Protoboard.as_view(), name='protoboard'),
    path('sensor.html/', Sensor.as_view(), name='sensor'),
    path('pic.html/', PIC.as_view(), name='pic'),
    path('componente/<str:component_name>/', ComponentDetailView.as_view(), name='component_detail'),
    path('send_email/<str:component_name>/', SendEmailView.as_view(), name='send_email'),
]


