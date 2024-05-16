from django.urls import path
from vehiculos.views import index, buscar_vehiculo, publicar_vehiculo

app_name = "vehiculos"

urlpatterns = [
    path("", index, name="index"),
    path('vehiculo/buscar', buscar_vehiculo, name='buscar_vehiculo'),  
    path('vehiculos/agregar', publicar_vehiculo, name='publicar_vehiculo'),
    ]