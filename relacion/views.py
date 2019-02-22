from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.
class IndexView(generic.ListView):
    model = models.Item
    context_object_name = 'lista_de_items'
    template_name = "relacion/index.html"

class DetailView(generic.DetailView):
    model = models.Item
    context_object_name = 'item'
    template_name = "relacion/detalle.html"

class BuscarView(generic.ListView):
    model = models.Item
    context_object_name = 'buscar'
    template_name = "relacion/buscar.html"

class EntradaView(generic.ListView):
    model = models.Item
    context_object_name = 'entrada'
    template_name = "relacion/entrada.html"

class SalidaView(generic.ListView):
    model = models.Item
    context_object_name = 'salida'
    template_name = "relacion/salida.html"

class CatalogoView(generic.ListView):
    model = models.Item
    context_object_name = 'catalogo'
    template_name = "relacion/catalogo.html"

class BorrarView(generic.DeleteView):
    model = models.Item
    context_object_name = 'borrar'
    template_name = "relacion/borrar.html"

