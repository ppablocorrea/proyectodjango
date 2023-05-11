from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Servicio
from .models import Socio
from .models import Empleado
from .models import Local
from .models import Ocupacion
from .models import Agenda

# Create your views here.

def registerPage(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            return redirect('/registro')
            messages.error(request, 'Las contraseñas no coinciden.')
        User.objects.create_user(username, email=email, first_name=name, last_name=last_name, password=password)
        return redirect('/login')
    return render(request, 'register.html')

def loginPage(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Se inició sesión correctamente.')
                return redirect('/')

        messages.error(request, 'Datos incorrectos.')
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('/')

def home(request):
    servicios = Servicio.objects.all()
    return render(request, 'home.html', {'servicios': servicios})

def mantenersocios(request):
    socios = Socio.objects.all()
    return render(request, 'mantenersocios.html', {'socios': socios})

def mantenerservicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'mantenerservicios.html', {'servicios': servicios})

def mantenerempleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'mantenerempleados.html', {'empleados': empleados})

def mantenerlocales(request):
    locales = Local.objects.all()
    return render(request, 'mantenerlocales.html', {'locales': locales})

def mantenerocupaciones(request):
    ocupaciones = Ocupacion.objects.all()
    return render(request, 'mantenerocupaciones.html', {'ocupaciones': ocupaciones})

def manteneragendas(request):
    agendas = Agenda.objects.order_by('-fecha')
    return render(request, 'manteneragendas.html', {'agendas': agendas})

def agenda(request, id = None):
    if request.method == 'POST':
        id = request.POST.get('id')
        fec = request.POST.get('fecha')
        if fec == '':
            fecha = None
        else:
            fecha = fec
        if id is None:
            socio_id = request.POST.get('socio')
            servicio_id = request.POST.get('servicio')
            empleado_id = request.POST.get('empleado')
            local_id = request.POST.get('local')
            Agenda.objects.create(
                fecha = fecha,
                socio = Socio.objects.get(id = socio_id),
                servicio = Servicio.objects.get(id = servicio_id),
                empleado = Empleado.objects.get(id = empleado_id),
                local = Local.objects.get(id = local_id),
                user = request.user
            )
            messages.success(request, 'Se ha realizado la agenda correctamente.')
            return redirect('/manteneragendas')
        else:
            p = Agenda.objects.get(id = id)
            if p.user == request.user:
                p.fecha = request.POST.get('fecha')
                socio_id = request.POST.get('socio')
                p.socio = Socio.objects.get(id = socio_id)
                servicio_id = request.POST.get('servicio')
                p.servicio = Servicio.objects.get(id = servicio_id)
                empleado_id = request.POST.get('empleado')
                p.empleado = Empleado.objects.get(id = empleado_id)
                local_id = request.POST.get('local')
                p.local = Local.objects.get(id = local_id)
                p.save()

    context = {}
    context['socios'] = Socio.objects.all()
    context['servicios'] = Servicio.objects.all() 
    context['empleados'] = Empleado.objects.all()  
    context['locales'] = Local.objects.all() 
    if id is not None:
        p = Agenda.objects.get(id = id)
        context['agenda'] = p
    return render(request, 'agenda.html', context)

def socio(request, id = None):
    if request.method == 'POST':
        id = request.POST.get('id')
        tel = request.POST.get('telefono')
        if tel == '':
            telefono = None
        else:
            telefono = tel
        if id is None:
            Socio.objects.create(
                nombre = request.POST.get('nombre'),
                apellido = request.POST.get('apellido'),
                telefono = telefono,
                email = request.POST.get('email')
            )
        else:
            p = Socio.objects.get(id = id)
            p.nombre = request.POST.get('nombre')
            p.apellido = request.POST.get('apellido')
            p.telefono = request.POST.get('telefono')
            p.email = request.POST.get('email')
            p.save()

    context = {}
    if id is not None:
        p = Socio.objects.get(id = id)
        context['socio'] = p
    return render(request, 'socio.html', context)

def servicio(request, id = None):
    if request.method == 'POST':
        id = request.POST.get('id')
        if id is None:
            Servicio.objects.create(
                nombre = request.POST.get('nombre'),
                descripcion = request.POST.get('descripcion'),
            )
        else:
            p = Servicio.objects.get(id = id)
            p.nombre = request.POST.get('nombre')
            p.descripcion = request.POST.get('descripcion') 
            p.save()

    context = {}
    if id is not None:
        p = Servicio.objects.get(id = id)
        context['servicio'] = p
    return render(request, 'servicio.html', context)

def empleado(request, id = None):
    if request.method == 'POST':
        id = request.POST.get('id')
        tel = request.POST.get('telefono')
        if tel == '':
            telefono = None
        else:
            telefono = tel
        if id is None:
            ocupacion_id = request.POST.get('ocupacion')
            Empleado.objects.create(
                nombre = request.POST.get('nombre'),
                apellido = request.POST.get('apellido'),
                telefono = telefono,
                email = request.POST.get('email'),
                ocupacion = Ocupacion.objects.get(id = ocupacion_id)
            )
        else:
            p = Empleado.objects.get(id = id)
            p.nombre = request.POST.get('nombre')
            p.apellido = request.POST.get('apellido')
            p.telefono = request.POST.get('telefono')
            p.email = request.POST.get('email')
            ocupacion_id = request.POST.get('ocupacion')
            p.ocupacion = Ocupacion.objects.get(id = ocupacion_id)
            p.save()

    context = {}
    context['ocupaciones'] = Ocupacion.objects.all() 
    if id is not None:
        p = Empleado.objects.get(id = id)
        context['empleado'] = p
    return render(request, 'empleado.html', context)

def local(request, id = None):
    if request.method == 'POST':
        id = request.POST.get('id')
        if id is None:
            Local.objects.create(
                nombre = request.POST.get('nombre'),
                direccion = request.POST.get('direccion'),
            )
        else:
            p = Local.objects.get(id = id)
            p.nombre = request.POST.get('nombre')
            p.direccion = request.POST.get('direccion') 
            p.save()

    context = {}
    if id is not None:
        p = Local.objects.get(id = id)
        context['local'] = p
    return render(request, 'local.html', context)

def ocupacion(request, id = None):
    if request.method == 'POST':
        id = request.POST.get('id')
        if id is None:
            Ocupacion.objects.create(
                nombre = request.POST.get('nombre'),
                descripcion = request.POST.get('descripcion'),
            )
        else:
            p = Ocupacion.objects.get(id = id)
            p.nombre = request.POST.get('nombre')
            p.descripcion = request.POST.get('descripcion') 
            p.save()

    context = {}
    if id is not None:
        p = Ocupacion.objects.get(id = id)
        context['ocupacion'] = p
    return render(request, 'ocupacion.html', context)

