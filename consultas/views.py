from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ConsultaForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from app.models import Complejo, Cliente
from .models import Consulta
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ConsultaForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


# Create your views here.
"""
#@method_decorator(staff_member_required, name = 'dispatch')
class ConsultaCreateView(CreateView):
    model = Consulta
    form_class = ConsultaForm
    success_url = reverse_lazy('complejos')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.cliente_id = self.request.user.id
        self.object.complejo_id = self.request.GET['id']
        form.save()        
        return super(ConsultaCreateView, self).form_valid(form)

"""

@method_decorator(staff_member_required, name='dispatch')
class ConsultaCreateView(CreateView):
    model = Consulta
    form_class = ConsultaForm
    success_url = reverse_lazy()

    def form_valid(self, form, **kargs):
        cliente = Cliente.objects.get(user_id = self.request.user.id)
        form.instance.cliente_id = cliente.id
        form.instance.complejo_id = self.kwargs['complejo_id']
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complejo = Complejo.objects.get(id = self.kwargs['complejo_id'])
        context['complejo'] = complejo
        return context
    
    def get_success_url(self, **kwargs):
        cliente = Cliente.objects.get(user_id = self.request.user.id)
        return reverse_lazy('consultas:listar_consultas', args = (cliente.id,))

# Busca las consultas por filtro, por ejemplo, por user.id
class ConsultasListView(ListView):
    model = Consulta

    def get_context_data(self):
        if Cliente.objects.filter(user_id = self.request.user.id).exists():
            cliente = Cliente.objects.get(user_id = self.request.user.id)
            return Consulta.objects.filter(cliente_id = cliente.id).order_by('-id')
        else:
            return None


class ConsultaDetailView(DetailView):
    model = Consulta

def ver_mi_consulta(request, id):

    consulta = get_object_or_404(Consulta, id=id)
    consulta.leida = True
    consulta.save()

    data = {
        'consulta':consulta,
        'form':ConsultaForm()
    }

    if request.method == 'POST':
        #formulario = ConsultaForm(data=request.POST, instance=consulta)

        messages.success(request,'Mensaje enviado!')
        return render(request, 'app/mis_consultas.html', data)


def BuscarComplejoXConsulta(id):
    complejo = Complejo()
    if id != None:
        complejo = Complejo.objects.get(id=id)
    return complejo

def BuscarConsultaXIdConsulta(id):
    consulta = get_object_or_404(Consulta, id=id)
    return consulta

def mis_consultas(request):
    cliente = Cliente.objects.get(user_id = request.user.id)
    lista_consultas = Consulta.objects.filter(cliente_id = cliente.id)
    lista_complejos = []
    for consulta in lista_consultas:
        lista_complejos.append(BuscarComplejoXConsulta(consulta.complejo_id))
    for complejo in lista_complejos:
        if complejo in lista_complejos:
            lista_complejos.remove(complejo)
    # consulta = Consulta()
    # consulta = BuscarConsultaXIdConsulta(id)
    # consulta.leida = True
    # consulta.save()

    # complejo = Complejo()
    # complejo = BuscarComplejoXConsulta(consulta.complejo_id)

    cliente = get_object_or_404(Cliente, user_id = request.user.id)
    #consultas = Consulta.objects.filter(Consulta, pk = cliente.id).orderby(id)
    consultas = Consulta.objects.all()
    consultas_form = []
    mensajes = []

    for c in consultas:
        if c.cliente_id == cliente.id:

            consultas_form.append(c)
            

    data = {
        'consultas':consultas_form,
        'mensajes':mensajes,
        #'consulta':consulta,
        'lista_consultas':lista_consultas,
        'lista_complejos':lista_complejos
    }

    return render(request,'consultas/mis_consultas.html', data)