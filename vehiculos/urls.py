from django.urls import path
from . import views

app_name = "vehiculos"

urlpatterns = [
    path("", views.index, name="index"),
    path('buscar_vehiculo/', views.buscar_vehiculo, name='buscar_vehiculo'),
    path('resultado_busqueda/', views.resultado_busqueda, name='resultado_busqueda'),
    ]