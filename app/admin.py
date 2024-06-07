from django.contrib import admin
from .models import Complejo, Cliente, Exterior, Servicio, Equipamiento
from django.contrib.auth.models import User

# Register your models here.

class ComplejoAdmin(admin.ModelAdmin):
    list_display = ['nombre_complejo','direccion','telefono','activo']
    list_editable = ['activo']
    search_fields = ['nombre_complejo']
    list_filter = ['activo']

class ExteriorAdmin(admin.ModelAdmin):
    list_display = ['complejo','terraza','piscina']

class ServicioAdmin(admin.ModelAdmin):
    list_display = ['complejo','luz','calefon']

class EquipamientoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'visible']

    

admin.site.register(Complejo, ComplejoAdmin)
admin.site.register(Cliente)
admin.site.register(Exterior, ExteriorAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Equipamiento, EquipamientoAdmin)