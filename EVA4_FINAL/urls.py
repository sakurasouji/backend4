"""
URL configuration for EVA4_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from reservasAPP.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('menu/', menu, name='menu'),
    
    #path('reservasAPI/', viewAPI.as_view(), name= 'crAPI'),
    path('reservasAPI/', viewAPI.listaReservaAPI, name= 'crAPI'),
    path('reservasAPI/update/<str:id>', viewAPI.updReservaAPI, name= 'updateAPI'), 
    path('reservasAPI/delete/<str:id>', viewAPI.delReservaAPI, name= 'deleteAPI'),
    
    path('listaReservas/', readReserva, name='listaReservas'),
    path('creaReserva/', createReserva, name='creaReserva'),
    path('listaReservas/editReserva/<int:id>', editReserva, name='editReserva'),
    path('delReserva/<int:id>', delReserva, name='delReserva'),
    
]
