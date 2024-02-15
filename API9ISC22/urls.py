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
from api.views import Informes
from api.views import Informacion
from api.views import Prueba
from api.views import Predial


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name='index'),
    path('informes.html',Informes.as_view(),name='informes'),
    path('informacion.html',Informacion.as_view(),name='informacion'),
    path('prueba.html',Prueba.as_view(),name='prueba'),
    path('p_predial.html',Predial.as_view(),name='p_predial'),
]



