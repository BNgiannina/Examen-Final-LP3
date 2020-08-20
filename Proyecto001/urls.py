"""Proyecto001 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('inicio/', views.index, name="inicio"),   
    path('estudiantes/',views.estudiantes, name="estudiantes"),
    path('consultas/',views.consultas, name="consultas"),
    path('listar-curso/', views.listar_cursos, name="listar_cursos"),
    path('eliminar-curso/<int:id>',views.eliminar_curso, name="eliminar_curso"),
    path('listar-carrera/', views.listar_carrera, name="listar_carrera"),
    path('eliminar-carrera/<int:id>',views.eliminar_carrera, name="eliminar_carrera"),
    path('listar-estudiantes/', views.listar_estudiantes, name="listar_estudiantes"),
    path('eliminar-estudiantes/<int:id>',views.eliminar_estudiantes, name="eliminar_estudiantes"),
  
]
