from django.contrib import admin

# Register your models here.

from .models import Local
from .models import Socio
from .models import Ocupacion
from .models import Servicio
from .models import Empleado
from .models import Agenda

admin.site.register(Local)
admin.site.register(Socio)
admin.site.register(Ocupacion)
admin.site.register(Servicio)
admin.site.register(Empleado)
admin.site.register(Agenda)
