"""
URL configuration for Proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista_consecionarios/',lista_consecionarios,name='lista_consecionarios'),
    path('lista_agentes/',lista_agentes,name='lista_agentes'),
    path('lista_vehiculos/',lista_vehiculos,name='lista_vehiculos'),
    path('consecionario_form/',consecionario_form,name='consecionario_form'),
    path('agente_form/',agente_form,name='agente_form'),
    path('vehiculo_form/',vehiculo_form,name='vehiculo_form'),
    path('buscar_agentes/',buscar_agentes,name='buscar_agentes'),
]
