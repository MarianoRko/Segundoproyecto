from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from .models import Reserva

def index(request):
    return render(request, 'web/index.html')

class ReservaListView(ListView):
    model = Reserva
    context_object_name = 'reserva_listado'
    template_name = 'web/reserva_listado.html'


class ReservaCreateView(CreateView):
    model = Reserva
    template_name = 'web/reserva_crear.html'
    success_url = 'listado'
    fields = '__all__'

class ReservaDetailView(DetailView):
    model = Reserva
    template_name = 'web/reserva_detalle.html'

class ReservaUpdateView(UpdateView):
    model = Reserva
    template_name = 'web/reserva_modificar.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('reserva_detalle', kwargs={'pk': self.object.pk})
    
class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'web/reserva_borrar.html'
    success_url = reverse_lazy('reserva_listado')
