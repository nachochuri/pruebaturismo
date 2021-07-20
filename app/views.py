from django.shortcuts import render, redirect, get_object_or_404
from .models import Complejo, Cliente, Consulta, Equipamiento, Exterior, Mensaje, Servicio
from .forms import ConsultaForm, MensajeForm, ExtendsUserCreationForm, ClienteForm
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mass_mail
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission, User, AnonymousUser

#from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    next = request.POST.get('next')

    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.id)

        if(hasattr(user, 'complejo')):
            return redirect(to='listar_consultas')
            

    complejos = Complejo.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(complejos, 8)
        complejos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity':complejos,
        'paginator':paginator
    }

    return render(request, 'app/home.html', data)

#@login_required(redirect_field_name = 'next')
@permission_required('app.add_consulta')
def realizar_consulta(request, nombre):
    
    complejo = get_object_or_404(Complejo, nombre_complejo=nombre)
    cliente = get_object_or_404(Cliente, user_id=request.user.id)
    
    
    data = {
        'consulta' : ConsultaForm(),
        'complejo' : complejo,
        'cliente': cliente,
        'mensaje': MensajeForm()
    }

    if request.method == 'POST':
        
        consulta = ConsultaForm(request.POST)
        mensaje = MensajeForm(request.POST)
        
        if consulta.is_valid():
            instanceC = consulta.save(commit=False)
            instanceC.cliente = cliente
            instanceC.complejo = complejo
            instanceC.leida = False
            instanceC.save()
            instanceM = mensaje.save(commit=False)
            
            instanceM.consulta = instanceC
            instanceM.creador = 0
            instanceM.save()
            #mensaje_complejo = ('Consulta desde TurismoReserva', instance.mensaje, 'TurismoReserva', ['restonacho@gmail.com'])
            #mensaje_central = ('Nueva consulta', 'Here is another message', 'TurismoReserva', ['ignacio@estudioweb.net'])
            #send_mass_mail((mensaje_complejo, mensaje_central), fail_silently=False)
            messages.success(request,'Consulta enviada!')
            return redirect(to='home')
        else:
            #data['complejo'] = complejo
            data['consulta'] = consulta
            data['mensaje'] = mensaje

    return render(request, 'app/realizar_consulta.html', data)

@permission_required('app.view_consulta')
def listar_consultas(request):
    usuario = request.user
    complejo = get_object_or_404(Complejo, user_id=usuario.id)
    
    consultas = Consulta.objects.filter(complejo = complejo)
    mensajes = Mensaje.objects.order_by('-id')[0]
    ultimo_msj = mensajes
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(consultas, 8)
        consultas = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity' : consultas,
        'ultimo_msj':ultimo_msj,
        'paginator' : paginator
    }

    return render(request, 'app/listar_consultas.html', data)

@permission_required('app.view_consulta')
def ver_consulta(request, id):

    consulta = get_object_or_404(Consulta, id=id)
    mensajes = Mensaje.objects.filter(consulta_id=id)
    consulta.leida = True
    consulta.save()
    
    data = {
        'consulta':consulta,
        'mensajes':mensajes,
        'form':ConsultaForm(),
        'msjform':MensajeForm()
    }

    if request.method == 'POST':
        #formulario = ConsultaForm(data=request.POST, instance=consulta)
        mensaje = MensajeForm(request.POST)

        if mensaje.is_valid():
            consulta.leida = False
            consulta.save()
            instanceM = Mensaje()
            instanceM = mensaje.save(commit=False)
            instanceM.consulta = consulta
            instanceM.creador = 1
            instanceM.save()

            messages.success(request,'Respuesta enviada!')
            return redirect(to='listar_consultas')
        

    return render(request, 'app/ver_consulta.html', data)


@permission_required('app.view_consulta')
def ver_mi_consulta(request, id):

    consulta = get_object_or_404(Consulta, id=id)
    mensajes = Mensaje.objects.filter(consulta_id=id)
    consulta.leida = True
    consulta.save()

    data = {
        'consulta':consulta,
        'mensajes':mensajes,
        'form':ConsultaForm(),
        'msjform':MensajeForm()
    }

    if request.method == 'POST':
        #formulario = ConsultaForm(data=request.POST, instance=consulta)
        mensaje = MensajeForm(request.POST)

        if mensaje.is_valid():
            consulta.leida = False
            consulta.save()
            instanceM = Mensaje()
            instanceM = mensaje.save(commit=False)
            instanceM.consulta = consulta
            instanceM.creador = 0
            instanceM.save()

            messages.success(request,'Mensaje enviado!')
    return render(request, 'app/ver_mi_consulta.html', data)

def prueba(request):
    return render(request, 'app/prueba.html')

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
            return redirect(to='home')
    else:
        form = ExtendsUserCreationForm()
        cliente_form = ClienteForm()

    data = {'form':form, 'cliente_form':cliente_form}

    return render(request, 'registration/registro.html', data)


def mis_consultas(request):
    cliente = get_object_or_404(Cliente, user_id = request.user.id)
    #consultas = Consulta.objects.filter(Consulta, pk = cliente.id).orderby(id)
    consultas = Consulta.objects.all()
    consultas_form = []
    
    for c in consultas:
        if c.cliente_id == cliente.id:
            consultas_form.append(c)

    data = {
        'consultas':consultas_form
    }

    return render(request,'app/mis_consultas.html', data)

def ver_cliente(request):
    data = {
        'form':ClienteForm()
    }
    return render(request,'app/ver_cliente.html',data)

def buscar_equipamientos(objeto):
    lista_equipamiento = []
    lista_equipamiento.append(objeto.heladera)
    lista_equipamiento.append(objeto.frigobar)
    lista_equipamiento.append(objeto.banio_suite)
    lista_equipamiento.append(objeto.mosquitero)
    lista_equipamiento.append(objeto.frazadas)
    lista_equipamiento.append(objeto.acolchado)
    lista_equipamiento.append(objeto.bidet)
    lista_equipamiento.append(objeto.ventiladores)
    lista_equipamiento.append(objeto.aire_acondicionado)
    lista_equipamiento.append(objeto.cofre)
    lista_equipamiento.append(objeto.secador_pelo)

    return lista_equipamiento

@login_required(redirect_field_name = 'next')
def ver_complejo(request, nombre):

    complejo = get_object_or_404(Complejo, nombre_complejo=nombre)
    #cliente = get_object_or_404(Cliente, user_id=request.user.id)
    equipamiento = get_object_or_404(Equipamiento, complejo_id = complejo.id)
    #exterior = get_object_or_404(Exterior, complejo_id = complejo.id)
    #servicio = get_object_or_404(Servicio, complejo_id = complejo.id)
    lista_equipamiento = buscar_equipamientos(equipamiento)

    data = {
        'complejo' : complejo,
        'equipamiento': equipamiento,
        'lista_equipamientos': lista_equipamiento
    }

    return render(request, 'app/ver_complejo.html', data)