from django.urls import path, include
from .views import (ConsultaCreateView, ConsultasListView, ConsultaDetailView, mis_consultas, ver_mi_consulta)
from django.contrib.auth.views import LogoutView

urlconsultas = ([
    path('realizar-consulta/<int:complejo_id>/<slug:nombre_complejo>/', ConsultaCreateView.as_view(), name='realizar_consulta'),
    path('listar-consultas/<int:id>', ConsultasListView.as_view(), name = 'listar_consultas'),
    path('ver-consulta/<int:pk>', ConsultaDetailView.as_view(), name = 'ver_consulta'),
    path('ver-mi-consulta/<id>', ver_mi_consulta, name = 'ver_mi_consulta'),
    path("logout/", LogoutView.as_view(), name="logout"),
    #path('mis-consultas/', mis_consultas, name='mis_consultas'),
], 'consultas')