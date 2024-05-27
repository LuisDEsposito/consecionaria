from django.urls import path
from vehiculos.views import (
    index,
    lista_vehiculos,
    publicar_vehiculo,
    detalle_vehiculo,
    editar_vehiculo,
    eliminar_vehiculo,
    )

app_name = "vehiculos"

urlpatterns = [
    path("", index, name="index"),
    path("lista/vehiculos", lista_vehiculos, name="lista_vehiculos"), 
    path('vehiculos/publicar', publicar_vehiculo, name='publicar_vehiculo'),
    path('vehiculo/detalle/<int:pk>', detalle_vehiculo, name='detalle_vehiculo'),
    path('vehiculo/editar/<int:pk>', editar_vehiculo, name='editar_vehiculo'),
    path('vehiculo/eliminar/<int:pk>', eliminar_vehiculo, name='eliminar_vehiculo'),
]