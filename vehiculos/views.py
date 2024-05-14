from django.shortcuts import render
from . import models

def index(request):
    consultar = models.Ver_vehiculos.objects.all()
    contexto = {'Ver_vehiculos': consultar}
    return render(request, "vehiculos/index.html", contexto)

def buscar_vehiculo(request):
    return render(request, "buscar_vehiculo.html")