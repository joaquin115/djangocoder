import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Curso
from .forms import NuevoCurso

# Create your views here.

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})

def crear_curso(request):

    # post
    if request.method == "POST":

        info_formulario = request.POST
        
        curso = Curso(nombre=info_formulario["nombre"], comision=int(info_formulario["comision"]))

        curso.save() # guardamos en la bd
        
        return redirect("cursos")

    else: # get y otros

        formularioVacio = NuevoCurso()

        return render(request,"ProyectoCoderApp/formulario_curso.html",{"form":formularioVacio})
    

def profesores(request):
    return render(request,"ProyectoCoderApp/profesores.html",{})

def estudiantes(request):
    return render(request,"ProyectoCoderApp/estudiantes.html",{})

def cursos(request):
    # return HttpResponse("Vista de cursos")

    cursos = Curso.objects.all()

    return render(request,"ProyectoCoderApp/cursos.html",{"cursos":cursos})


def base(request):
    return render(request,"ProyectoCoderApp/base.html",{})

def entregables(request):
    return HttpResponse("Vista de entregables")