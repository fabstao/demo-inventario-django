from . import views
from django.urls import path

app_name = 'administracion'
urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('<int:pk>/',views.DetailView.as_view(), name='detalle'),
]