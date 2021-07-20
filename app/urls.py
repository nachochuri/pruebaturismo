from django.urls import path, include
from .views import home, realizar_consulta, listar_consultas, ver_consulta, registro, mis_consultas, ver_cliente, ver_mi_consulta, ver_complejo

urlpatterns = [
    path('home/', home, name = 'home'),
    path('realizar-consulta/<nombre>', realizar_consulta, name='realizar_consulta'),
    path('listar-consultas/', listar_consultas, name = 'listar_consultas'),
    path('ver-consulta/<id>', ver_consulta, name = 'ver_consulta'),
    path('ver-mi-consulta/<id>', ver_mi_consulta, name = 'ver_mi_consulta'),
    path('accounts/', include('django.contrib.auth.urls'),),
    path('registro/', registro, name='registro'),
    path('mis-consultas/', mis_consultas, name='mis_consultas'),
    path('ver-cliente/', ver_cliente, name='ver_cliente'),
    path('ver-complejo/<nombre>', ver_complejo, name='ver_complejo'),
]