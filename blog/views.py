from django.shortcuts import render
from django.http import HttpResponse

import datetime

from .models import *
from .forms import *

# Create your views here.

def inicio(request):
    saludar = "Bienvenidos al blog"
    return HttpResponse(saludar)

def usuarioForm(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            email = form.cleaned_data["email"]
            apodo = form.cleaned_data["apodo"]
            usuario = Usuario(nombre=nombre, apellido=apellido, email=email, apodo=apodo)
            usuario.save()
            form = UsuarioForm()
            
    else:
        form = UsuarioForm()
    return render(request, "blog/carga_de_usuarios.html", {"form":form})   

def publicaciones(request):
    if request.method == "POST":
        form = PublicacionesForm(request.POST)
        if form.is_valid():
            titulo_de_publicacion = form.cleaned_data["titulo_de_publicacion"]
            publicacion = form.cleaned_data["publicacion"]
            fecha_de_publicacion = form.cleaned_data["fecha_de_publicacion"]
            posteo = Publicaciones(titulo_de_publicacion=titulo_de_publicacion, publicacion=publicacion, fecha_de_publicacion=fecha_de_publicacion)
            posteo.save()
            
            form = PublicacionesForm()
            
    else:
        form = PublicacionesForm()
    return render(request, "blog/publicaciones.html", {"form":form})     


def adminForm(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            email = form.cleaned_data["email"]
            administrador = Administrador(nombre=nombre, apellido=apellido, email=email)
            administrador.save()
            
            form = AdminForm()
            
    else:
        form = AdminForm()
    return render(request, "blog/carga_de_admin.html", {"form":form})   

def listadoDeAdministradores(request):
    administradores = Administrador.objects.all()
    return render(request, "blog/listado_de_admin.html", {"administradores":administradores})

def buscar_publicaciones(request):
    query = request.GET.get('q')
    resultados = []

    if query:
        resultados = Publicaciones.objects.filter(titulo_de_publicacion__icontains=query)

    return render(request, 'blog/buscador_de_publicaciones.html', {'resultados': resultados, 'query': query})
