from django.shortcuts import render
from .models import Categoria
from django.http import HttpResponse
from django.template import loader
import datetime

def categoria(req,nombre):
    categoria = Categoria(nombre=nombre)
    categoria.save()

    return HttpResponse (f""" <p>Categoria: {categoria.nombre}<p>""")

def lista_categorias(req):
    lista = Categoria.objects.all()
    return render(req, "lista_categorias.html", {"lista_categorias":lista})

