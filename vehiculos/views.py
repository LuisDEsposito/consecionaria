from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from vehiculos.models import Ver_vehiculos, Marcas
from vehiculos.forms import Ver_vehiculosform
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

# INICIO
def index(request):
    return render(request, "vehiculos/index.html")


# LISTA
class Ver_vehiculosList(ListView):
    model = Ver_vehiculos
    context_object_name = "vehiculos"
    template_name = "vehiculos/lista_vehiculos.html"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Ver_vehiculos.objects.filter(marcas__icontains=busqueda)
        return queryset


# PUBLICAR VEHICULO:
class Ver_vehiculosCreate(CreateView):
    model = Ver_vehiculos
    form_class = Ver_vehiculosform
    template_name = "vehiculos/lista_vehiculos_form.html"
    success_url = reverse_lazy("vehiculos:lista_vehiculos")

#VER DETALLE
class Ver_vehiculosDetail(DetailView):
    model = Ver_vehiculos
    context_object_name = "vehiculo"
    template_name = "vehiculos/lista_vehiculos_detalle.html"

#ACTUALIZAR DATOS.
class Ver_vehiculosUpdate(UpdateView):
    model = Ver_vehiculos
    form_class = Ver_vehiculosform
    template_name = "vehiculos/lista_vehiculos_form.html"
    success_url = reverse_lazy("vehiculos:lista_vehiculos")

# ELIMINAR DATOS:
class Ver_vehiculosDelete(DeleteView):
    model = Ver_vehiculos
    context_object_name = "vehiculo"
    template_name = "vehiculos/lista_vehiculos_confirmar_eliminar.html"
    success_url = reverse_lazy("vehiculos:lista_vehiculos")


# FORMATO VIEJO EN CASO DE FALLAS.

# LISTA
# def lista_vehiculos(request):
#     busqueda = request.GET.get("busqueda")
#     if busqueda:
#         print(busqueda)
#         consulta = Ver_vehiculos.objects.filter(marcas__icontains=busqueda)
#     else:
#         consulta = Ver_vehiculos.objects.all()
#     contexto = {'vehiculos': consulta}
#     return render(request, "vehiculos/lista_vehiculos.html", contexto)


# PUBLICAR VEHICULO:
# def publicar_vehiculo(request):
#     if request.method == "POST":
#         form = Ver_vehiculosform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect ("vehiculos:lista_vehiculos")
#     else:
#         form = Ver_vehiculosform()
#     return render (request, "vehiculos/lista_vehiculos_form.html", {"form": form})


#VER DETALLE
# def detalle_vehiculo(request, pk: int):
#     consulta = Ver_vehiculos.objects.get(id=pk)
#     contexto = {"vehiculo": consulta}
#     return render(request, "vehiculos/lista_vehiculos_detalle.html", contexto)


# ACTUALIZAR DATOS.
# def editar_vehiculo(request, pk : int):
#     consulta = Ver_vehiculos.objects.get(id=pk)
#     if request.method == "POST":
#         form = Ver_vehiculosform(request.POST, instance = consulta)
#         if form.is_valid():
#             form.save()
#             return redirect ("vehiculos:lista_vehiculos")
#     else:
#         form = Ver_vehiculosform(instance=consulta)
#     return render (request, "vehiculos/lista_vehiculos_form.html", {"form": form})


# ELIMINAR DATOS: 
# def eliminar_vehiculo(request, pk : int):
#     consulta = Ver_vehiculos.objects.get(id=pk)
#     if request.method == "POST":
#         consulta.delete()
#         return redirect("vehiculos:lista_vehiculos")
#     return render(request, "vehiculos/lista_vehiculos_confirmar_eliminar.html", {"object" : consulta})