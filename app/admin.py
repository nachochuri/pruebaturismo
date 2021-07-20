from django.contrib import admin
from .models import Complejo, Cliente, Consulta, Mensaje, Exterior, Servicio, Equipamiento
from django.contrib.auth.models import User

# Register your models here.

class ComplejoAdmin(admin.ModelAdmin):
    list_display = ['nombre_complejo','direccion','telefono','activo']
    list_editable = ['activo']
    search_fields = ['nombre_complejo']
    list_filter = ['activo']

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'complejo', 'fecha_ingreso', 'fecha_salida', 'cantidad_mayores', 'cantidad_menores', 'leida']
    search_fields = ['nombre']
    list_filter = ['complejo']
    list_per_page = 10

class MensajeAdmin(admin.ModelAdmin):
    list_display = ['mensaje', 'fecha', 'creador']

class ExteriorAdmin(admin.ModelAdmin):
    list_display = ['complejo','terraza','piscina']

class ServicioAdmin(admin.ModelAdmin):
    list_display = ['complejo','luz','calefon']

class EquipamientoAdmin(admin.ModelAdmin):
    list_display = ['complejo','heladera','frigobar']
    

admin.site.register(Complejo, ComplejoAdmin)
admin.site.register(Cliente)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Exterior, ExteriorAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Equipamiento, EquipamientoAdmin)