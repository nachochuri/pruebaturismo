from django.contrib import admin
from .models import Consulta

# Register your models here.
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'complejo', 'fecha_ingreso', 'fecha_salida', 'cantidad_mayores', 'cantidad_menores', 'leida']
    search_fields = ['nombre']
    list_filter = ['complejo']
    list_per_page = 10

class MyAdminSite(admin.AdminSite):

    def has_permission(request):
        return request.user.is_active and request.user.is_superuser
    
admin.site.register(Consulta, ConsultaAdmin)