from django.contrib import auth
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from .models import Complejo, localidades
from .forms import ExtendsUserCreationForm, ClienteForm
from django.contrib import messages
#from django.core.mail import send_mass_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, UpdateView
from django import forms

#from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class ComplejosListView(ListView):
    model = Complejo


class LoginComplejoView(DetailView):
    model = Complejo
    template_name = 'app/login.html'

class ComplejoUpdate(UpdateView):
    model = Complejo
    


"""
def registro(request):
    
    if request.method == 'POST':
        form = ExtendsUserCreationForm(request.POST)
        cliente_form = ClienteForm(request.POST)

        if form.is_valid() and cliente_form.is_valid():
            user = form.save()
            cliente = cliente_form.save(commit=False)
            cliente.user = user
            cliente.save()     

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
    
            
            user.user_permissions.add(33)
            user.user_permissions.add(40)
            user.user_permissions.add(36)
            user.user_permissions.add(37)
            
            messages.success(request,'Te has registrado!')
            return redirect(to='complejos')
    else:
        form = ExtendsUserCreationForm()
        cliente_form = ClienteForm()

    data = {'form':form, 'cliente_form':cliente_form}

    return render(request, 'registration/registro.html', data)
"""
def ver_cliente(request):
    data = {
        'form':ClienteForm()
    }
    return render(request,'app/ver_cliente.html',data)



"""
MOSTRAR INFO DE UN COMPLEJO SELECCIONADO
"""

class ComplejoDetailView(DetailView):
    model = Complejo


def login_complejo(request):
    
    if request.method == 'POST':
        
        
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if not Complejo.objects.filter(user_id = user.id).exists():
                raise forms.ValidationError('ERROR!!!')
            else:
                login(request, user)
                complejo = Complejo.objects.get(user_id = user.id)
                return redirect('complejo-admin/'+complejo.nombre_complejo)
        else:
            return redirect('login')
        
    else:
        form = AuthenticationForm()

    return render(request, 'app/login.html', {'form':form})
"""
def login_consulta(request,id):
    proxima = '../ver-complejo/'+str(id)
    if request.method == 'POST':
        id = str(request.GET.get('id'))
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to=proxima)
        else:
            messages.success(request,'Usuario o contraseña invalidos...')
            
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login_consulta.html/', {'form':form})

def logout_usuario(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect(to='http://localhost:8000/')

def nuevo_login(request):
    return render(request,'ver_complejo.html',{'form':AuthenticationForm})

    """





def autocomplete(request):
    datos = request.GET.get('term')
    #complejos = Complejo.objects.filter(nombre_complejo__icontains=datos)
    #lista_complejos = []
    #lista_complejos += [x.nombre_complejo for x in complejos]
    lista_localidades = []
    for key,value in localidades:
        if value.lower().__contains__(datos):
            lista_localidades.append(value)
    return JsonResponse(lista_localidades,safe=False)

def ver_complejos_por_localidad(request, lugar):
    loc = ''
    for key,value in localidades:
        if lugar == value:
            loc = key

    complejos = Complejo.objects.filter(localidad=loc)
    return render(request,'app/ver_complejos_por_localidad.html',{'complejos':complejos, 'localidad':lugar})
   