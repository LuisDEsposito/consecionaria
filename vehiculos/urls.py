from django.urls import path
from vehiculos.views import (
    Ver_vehiculosCreate, Ver_vehiculosList, 
    Ver_vehiculosDetail, Ver_vehiculosUpdate, 
    Ver_vehiculosDelete,)

app_name = "vehiculos"


from vehiculos.views import (
    index,
    # lista_vehiculos,
    # publicar_vehiculo,
    # detalle_vehiculo,
    # editar_vehiculo,
    # eliminar_vehiculo,
    )


urlpatterns = [
    path("", index, name="index"),
    # path("lista/vehiculos", lista_vehiculos, name="lista_vehiculos"), 
    # path('vehiculos/publicar', publicar_vehiculo, name='publicar_vehiculo'),
    # path('vehiculo/detalle/<int:pk>', detalle_vehiculo, name='detalle_vehiculo'),
    # path('vehiculo/editar/<int:pk>', editar_vehiculo, name='editar_vehiculo'),
    # path('vehiculo/eliminar/<int:pk>', eliminar_vehiculo, name='eliminar_vehiculo'),
]

# VISTAS BASADAS EN CLASES
urlpatterns += [
    path("lista/vehiculos", Ver_vehiculosList.as_view(), name = "lista_vehiculos"),
    path('vehiculos/publicar', Ver_vehiculosCreate.as_view(), name='publicar_vehiculo'),
    path('vehiculo/detalle/<int:pk>', Ver_vehiculosDetail.as_view(), name='detalle_vehiculo'),
    path('vehiculo/editar/<int:pk>', Ver_vehiculosUpdate.as_view(), name='editar_vehiculo'),
    path('vehiculo/eliminar/<int:pk>', Ver_vehiculosDelete.as_view(), name='eliminar_vehiculo'),
]