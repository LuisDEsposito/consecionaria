from django.shortcuts import render
from . import models
from vehiculos.models import Ver_vehiculos, Marcas

def index(request):
    consultar = Ver_vehiculos.objects.all()
    contexto = {'vehiculos': consultar}
    return render(request, "vehiculos/lista_vehiculos.html", contexto)


def buscar_vehiculo(request):
    return render(request, "vehiculos/buscar_vehiculo.html")


def resultado_busqueda(request):
    if request.get("marca"):
        marca_solicitada = request.get("marca")
        contexto = {'coincidencias' : Marcas.objects.filter(nombre_icontrains=marca_solicitada)}
        
        return render(request, "vehiculos/buscar_vehiculo.html", contexto)
    
    else:
        return f"Lo siento, no se encontraron resultados para tu busqueda."
    
