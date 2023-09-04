from django.shortcuts import render
from .models import Categoria, Cliente, Producto, Pedido
from django.http import HttpResponse, HttpRequest
from django.template import loader
import datetime
from django.core.exceptions import ObjectDoesNotExist
from .forms import ClienteFormulario, AgregaProductoFormulario, AgregaCategoriaFormulario

def categoria(req,nombre):
    categoria = Categoria(nombre=nombre)
    categoria.save()
    return HttpResponse (f""" <p>Categoria: {categoria.nombre}<p>""")

def lista_categorias(req):
    lista = Categoria.objects.all()
    return render(req, "lista_categorias.html", {"lista_categorias":lista})

def agregacategoria(req: HttpRequest):
    print('method', req.method)
    print('post', req.POST)
    if req.method == 'POST':
        miFormulariocategoria = AgregaCategoriaFormulario(req.POST)
        if miFormulariocategoria.is_valid():
            print(miFormulariocategoria.cleaned_data)
            data = miFormulariocategoria.cleaned_data
            categoria= Categoria(nombre=data["nombre"])
            categoria.save()
            return render(req, "inicio.html", {"mensaje": "Categoria creado con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})    
    else:
        miFormulariocategoria = AgregaCategoriaFormulario()
        return render(req, "agregacategoria.html", {"miFormulariocategoria": miFormulariocategoria})
    


def inicio(req):
    return render(req, "inicio.html")


def producto(req):
    return render(req, "produto.html")

def producto(req,nombre):
    producto = Producto(nombre=nombre)
    producto.save()
    return HttpResponse (f""" <p>Cliente: {producto.nombre}<p>""")

def lista_productos(req):
    lista = Producto.objects.all()
    return render(req, "producto.html", {"lista_productos":lista})

def agregarproducto(req: HttpRequest):
    print('method', req.method)
    print('post', req.POST)
    if req.method == 'POST':
        miFormularioproducto =  AgregaProductoFormulario(req.POST)
        if miFormularioproducto.is_valid():
            print(miFormularioproducto.cleaned_data)
            data = miFormularioproducto.cleaned_data
            producto = Producto(nombre=data["nombre"], precio=data["precio"])
            producto.save()
            return render(req, "inicio.html", {"mensaje": "Producto creado con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})  
    else:
        miFormularioproducto = AgregaProductoFormulario()
        return render(req, "agregaproducto.html", {"miFormularioproducto": miFormularioproducto})
    


def cliente(req,nombre):
    cliente = Cliente(nombre=nombre)
    cliente.save()
    return HttpResponse (f""" <p>Cliente: {cliente.nombre}<p>""")

def lista_clientes(req):
    lista = Cliente.objects.all()
    return render(req, "cliente.html", {"lista_clientes":lista})

def formulario(req: HttpRequest):
    print('method', req.method)
    print('post', req.POST)
    if req.method == 'POST':
        miFormulario = ClienteFormulario(req.POST)
        if miFormulario.is_valid():
            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data
            cliente = Cliente(nombre=data["nombre"], correo=data["correo"], direccion=data["direccion"])
            cliente.save()
            return render(req, "inicio.html", {"mensaje": "Cliente creado con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:
        miFormulario = ClienteFormulario()
        return render(req, "formulario.html", {"miFormulario": miFormulario})


def busquedacliente(req):
    return render(req, "busqueda_cliente.html")

def buscarcliente(req):

    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        cliente = Cliente.objects.get (nombre=nombre)
        return render(req,"resultadobuscar.html",{"cliente": cliente})   
    else:
        return HttpResponse ('no escribiste ningun cliente')


def pedido(req,nombre):
    pedido = Pedido(nombre=nombre)
    pedido.save()
    return HttpResponse (f""" <p>Pedido: {pedido.nombre}<p>""")

def lista_pedidos(req):
    lista = Pedido.objects.all()
    return render(req, "pedido.html", {"lista_pedidos":lista})


