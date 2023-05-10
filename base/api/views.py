from ..models import Socio
from django.http import JsonResponse

def routes(request):
    routes = [
        'GET /api/socios',
        'GET /api/socio/:id'
    ]
    return JsonResponse(routes, safe=False)

def socios(request):
    socios = Socio.objects.all()
    socios_dict = []
    for p in socios:
        socios_dict.append({
            'nombre': p.nombre,
            'apellido': p.apellido,
            'telefono': p.telefono,
            'email': p.email
        })
    return JsonResponse(socios_dict, safe=False)

def socio(request, id):
    socio = Socio.objects.get(id = id)
    socio_dict = {
        'nombre': socio.nombre,
        'apellido': socio.apellido,
        'telefono': socio.telefono,
        'email': socio.email
    }
    return JsonResponse(socio_dict, safe=False)