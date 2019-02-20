from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.

class IndexView(generic.ListView):
    model = models.Bodegas
    context_object_name = 'lasbodegas'
    template_name = 'administracion/index.html'


class DetailView(generic.DetailView):
    model = models.Bodegas
    context_object_name = 'bodega'
    template_name = 'administracion/detalle.html'