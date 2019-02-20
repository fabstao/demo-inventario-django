from django.urls import path



from . import views

app_name = 'relacion'
urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('<int:pk>/',views.DetailView.as_view(), name='detalle'),
    path('<int:pk>/buscar/',views.BuscarView.as_view(), name='buscar'),
    path('<int:pk>/entrada/',views.EntradaView.as_view(), name='entrada'),
    path('<int:pk>/salida/',views.SalidaView.as_view(), name='salida'),
    path('<int:pk>/borrar/',views.BorrarView.as_view(), name='borrar'),
    path('catalogo/',views.CatalogoView.as_view(), name='catalogo'),
    #path('catalogo/nuevo',views.BorrarView.as_view('nuevo'),
]
    
