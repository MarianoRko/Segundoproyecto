from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listado', views.ReservaListView.as_view(), name='reserva_listado'),
    path('crear', views.ReservaCreateView.as_view(), name='reserva_crear'),
    path('detalle/<pk>', views.ReservaDetailView.as_view(), name='reserva_detalle'),
    path('modificar/<pk>', views.ReservaUpdateView.as_view(), name='reserva_modificar'),
    path('borrar/<pk>', views.ReservaDeleteView.as_view(), name='reserva_borrar'),
]

