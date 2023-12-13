from django.urls import path,include
from django.contrib import admin


urlpatterns = [
    path('',include('inventario.urls')),
    path('usuarios/',include('usuarios.urls')),
    path('usuarios/',include('django.contrib.auth.urls')),

]

