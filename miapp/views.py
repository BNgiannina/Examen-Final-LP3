from django.shortcuts import render

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
