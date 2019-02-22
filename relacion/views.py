from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "relacion/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        litems = models.Item.objects.all()[:5]
        lstock = models.Movimiento.objects.all()[:5]
        cant = {}
        i = 0
        print(litems)
        print(lstock)
        for lit in litems:
            for stk in lstock:
                if lit.id == stk.item.id:
                    if str(stk.movimiento) == "entrada":
                        i+=stk.cantidad
                    if str(stk.movimiento) == "salida":
                        i-=stk.cantidad
                    print(i)
                    cant[lit.nombre] = i
        context['lista_de_items'] = models.Item.objects.all()[:5]
        context['stock'] = models.Movimiento.objects.all()[:5]
        context['cantidades'] = cant
        return context    

class oldIndexView(generic.ListView):
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

