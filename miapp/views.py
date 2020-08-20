from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Curso
from django.db.models import Q

# Create your views here.
layout = """

"""
def cursos(request):
    return render(request,'cursos.html',{
        'titulo':'cursos'
    })

def estudiantes(request):
 
   return render(request,'estudiantes.html',{
       'titulo':'estudiantes'
    })
def carreras(request):
    
   return render(request,'carreras.html',{
       'titulo':'carreras'
    })

def index(request):
 
   return render(request,'index.html',{
       'titulo':'index'
    })

def consultas(request):
 
   return render(request,'consultas.html',{
       'titulo':'consultas'
    })


def listar_cursos(request):

    cursos = Curso.objects.all()    
    return render(request,'listar_cursos.html',{
        'cursos': cursos,
        'titulo': 'Lista de Cursos'
    })

def eliminar_curso(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('listar_cursos')