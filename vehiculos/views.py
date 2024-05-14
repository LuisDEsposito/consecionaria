from django.shortcuts import render
from . import models
from django.http import HttpResponse
from .models import Marcas

def index(request):
    consultar = models.Ver_vehiculos.objects.all()
    contexto = {'Ver_vehiculos': consultar}
    return render(request, "vehiculos/index.html", contexto)

def buscar_vehiculo(request):
    return render(request, "vehiculos/buscar_vehiculo.html")

def resultado_busqueda(request):

    if request.GET("marca"):
        # mensaje = "Usted a ingresado: %r" %request.GET("marca")
        marca_solicitada = request.Get("marca")
        marcas_disponibles = Marcas.objects.filter(nombre_icontrains=marca_solicitada)
        
        return render(request, "buscar_vehiculo.html", )
    
    else:
        mensaje = "Lo siento, no se encontraron resultados para tu busqueda."
    
    return HttpResponse(mensaje)
