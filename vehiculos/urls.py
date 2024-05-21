from django.urls import path
from vehiculos.views import index, publicar_vehiculo

app_name = "vehiculos"

urlpatterns = [
    path("", index, name="index"), 
    path('vehiculos/publicar', publicar_vehiculo, name='publicar_vehiculo'),
    ]