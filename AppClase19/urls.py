from django.urls import path
from AppClase19.views import categoria, lista_categorias, inicio, producto, cliente, buscarcliente,formulario, busquedacliente, lista_productos, lista_clientes, lista_pedidos, agregarproducto,agregacategoria
urlpatterns = [
    #path('agrega-categoria/<nombre>', categoria),
    path('agregar-categorias', agregacategoria, name='agregar-categorias'),
    path('lista-categoria/', lista_categorias, name='categorias'),
    path('', inicio, name='inicio'),
    path('productos', lista_productos, name='productos'),
    path('agregar-productos', agregarproducto, name='agregar-productos'),
    path('clientes', lista_clientes, name='clientes'),
    path('agregar-clientes', formulario, name='agregar-clientes'),
    path('busqueda-clientes', busquedacliente, name='busqueda-clientes'),
    path('buscar-clientes/', buscarcliente, name='buscar-clientes')
    #path('pedidos', lista_pedidos, name='pedidos'),
    #path('buscar-clientes/', buscar_clientes, name='buscar_clientes'),
]   



