from django.shortcuts import render, redirect
from . import models
from vehiculos.models import Ver_vehiculos, Marcas
from vehiculos.forms import Ver_vehiculosform


def index(request):
    busqueda = request.GET.get("busqueda")
    if busqueda:
        print(busqueda)
        consulta = Ver_vehiculos.objects.filter(marcas__icontains=busqueda)
    else:
        consulta = Ver_vehiculos.objects.all()
    contexto = {'vehiculos': consulta}
    return render(request, "vehiculos/lista_vehiculos.html", contexto)

def publicar_vehiculo(request):
    if request.method == "POST":
        form = Ver_vehiculosform(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("vehiculos:index")
    else:
        form = Ver_vehiculosform()
    return render (request, "vehiculos/lista_vehiculos_agregar.html", {"form": form})


#     return render(request, "vehiculos/buscar_vehiculo.html")
# def resultado_busqueda(request):
#     if request.get("marca"):
#         marca_solicitada = request.get("marca")
#         contexto = {'coincidencias' : Marcas.objects.filter(nombre_icontrains=marca_solicitada)}
#         return render(request, "vehiculos/buscar_vehiculo.html", contexto)
    
#     else:
#         return f"Lo siento, no se encontraron resultados para tu busqueda."
    
