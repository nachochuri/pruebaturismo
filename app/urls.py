from django.contrib.auth import login
from django.urls import path, include
from .views import (ver_cliente, autocomplete,ver_complejos_por_localidad)
from .views import ComplejosListView, ComplejoDetailView, LoginComplejoView, login_complejo, ComplejoUpdate
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', ComplejosListView.as_view(), name = 'complejos'),
    #path('accounts/', include('django.contrib.auth.urls'),),
    path("logout/", LogoutView.as_view(), name="logout"),
    #path('registro/', registro, name='registro'),
    path('ver-cliente/', ver_cliente, name='ver_cliente'),
    path('complejo/<int:pk>/<slug:nombre_complejo>/', ComplejoDetailView.as_view(), name='complejo'),
    path('autocomplete', autocomplete, name='autocomplete'),
    path('ver-complejos-por-localidad/<lugar>', ver_complejos_por_localidad, name='ver_complejos_por_localidad'),
    path('complejo-admin/', login_complejo, name='login_complejo'),
    path('complejo-update/<int:pk>/', ComplejoUpdate.as_view(), name='complejo-update'),
]