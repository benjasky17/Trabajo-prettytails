"""
URL configuration for prettytails project.

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

from django.urls import path
from . import views
from .views import home, Perfil, exit, register, nosotros, NMascotas, detalle_perfil, infomascotas

urlpatterns = [
   path('',home, name='home'),
   path('Perfil/', Perfil, name='Perfil'),
   path('logout/', exit, name='exit'),
   path('register', register, name='register'),
   path('nosotros/', nosotros, name='nosotros'),
   path('NMascotas/', NMascotas, name='NMascotas'),
   path('detalle_perfil/', detalle_perfil, name='detalle_perfil'),
   path('infomascotas/', infomascotas, name='infomascotas'),
 
]
