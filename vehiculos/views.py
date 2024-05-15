from django.shortcuts import render
from . import models
from vehiculos.models import Ver_vehiculos

def index(request):
    consultar = Ver_vehiculos.objects.all()
    contexto = {'vehiculos': consultar}
    return render(request, "vehiculos/lista_vehiculos.html", contexto)

def buscar_vehiculo(request):
    return render(request, "vehiculos/buscar_vehiculo.html")

# def resultado_busqueda(request):

#     if request.get("marca"):
#         # mensaje = "Usted a ingresado: %r" %request.GET("marca")
#         marca_solicitada = request.get("marca")
#         marcas_disponibles = Marcas.objects.filter(nombre_icontrains=marca_solicitada)
        
#         return render(request, "buscar_vehiculo.html", )
    
#     else:
#         mensaje = "Lo siento, no se encontraron resultados para tu busqueda."
    
#     return HttpResponse(mensaje)
