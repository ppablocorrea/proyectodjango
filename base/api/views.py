from ..models import Local
from ..models import Servicio
from ..models import Ocupacion
from django.http import JsonResponse

def routes(request):
    routes = [
        'GET /api/locales',
        'GET /api/local/:id',
        'GET /api/servicios',
        'GET /api/servicio/:id',
        'GET /api/ocupaciones',
        'GET /api/ocupacion/:id'
    ]
    return JsonResponse(routes, safe=False)

def locales(request):
    locales = Local.objects.all()
    locales_dict = []
    for p in locales:
        locales_dict.append({
            'nombre': p.nombre,
            'direccion': p.direccion
        })
    return JsonResponse(locales_dict, safe=False)

def servicios(request):
    servicios = Servicio.objects.all()
    servicios_dict = []
    for p in servicios:
        servicios_dict.append({
            'nombre': p.nombre,
            'descripcion': p.descripcion
        })
    return JsonResponse(servicios_dict, safe=False)

def ocupaciones(request):
    ocupaciones = Ocupacion.objects.all()
    ocupaciones_dict = []
    for p in ocupaciones:
        ocupaciones_dict.append({
            'nombre': p.nombre,
            'descripcion': p.descripcion
        })
    return JsonResponse(ocupaciones_dict, safe=False)

def local(request, id):
    local = Local.objects.get(id = id)
    local_dict = {
        'nombre': local.nombre,
        'direccion': local.direccion
    }
    return JsonResponse(local_dict, safe=False)

def servicio(request, id):
    servicio = Servicio.objects.get(id = id)
    servicio_dict = {
        'nombre': servicio.nombre,
        'descripcion': servicio.descripcion
    }
    return JsonResponse(servicio_dict, safe=False)

def ocupacion(request, id):
    ocupacion = Ocupacion.objects.get(id = id)
    ocupacion_dict = {
        'nombre': ocupacion.nombre,
        'descripcion': ocupacion.descripcion
    }
    return JsonResponse(ocupacion_dict, safe=False)