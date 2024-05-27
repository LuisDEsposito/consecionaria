from django.shortcuts import render, redirect
from vehiculos.models import Ver_vehiculos, Marcas
from vehiculos.forms import Ver_vehiculosform


def index(request):
    return render(request, "vehiculos/index.html")


def lista_vehiculos(request):
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
            return redirect ("vehiculos:lista_vehiculos")
    else:
        form = Ver_vehiculosform()
    return render (request, "vehiculos/lista_vehiculos_form.html", {"form": form})


def detalle_vehiculo(request, pk: int):
    consulta = Ver_vehiculos.objects.get(id=pk)
    contexto = {"vehiculo": consulta}
    return render(request, "vehiculos/lista_vehiculos_detalle.html", contexto)


def editar_vehiculo(request, pk : int):
    consulta = Ver_vehiculos.objects.get(id=pk)
    if request.method == "POST":
        form = Ver_vehiculosform(request.POST, instance = consulta)
        if form.is_valid():
            form.save()
            return redirect ("vehiculos:lista_vehiculos")
    else:
        form = Ver_vehiculosform(instance=consulta)
    return render (request, "vehiculos/lista_vehiculos_form.html", {"form": form})


def eliminar_vehiculo(request, pk : int):
    consulta = Ver_vehiculos.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("vehiculos:lista_vehiculos")
    return render(request, "vehiculos/lista_vehiculos_confirmar_eliminar.html", {"object" : consulta})