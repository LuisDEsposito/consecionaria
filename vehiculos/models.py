from django.db import models
from django.utils import timezone

class Tipo(models.Model):
    tipo = models.CharField(max_length= 255, unique=True)

    def __str__(self) -> str:
        return self.tipo
    
    class Meta:
        verbose_name = "Tipo de vehiculo"
        verbose_name_plural = "Tipos de vehiculo"


class Marcas(models.Model):
    marca = models.CharField(max_length= 255, unique=True)

    def __str__(self) -> str:
        return self.marca
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"


class Modelos(models.Model):
    modelo = models.CharField(max_length= 255, unique=True)

    def __str__(self) -> str:
        return self.modelo
    
    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"
        

class Ver_vehiculos(models.Model):
    tipo = models.CharField(max_length=50)
    modelos = models.CharField(max_length=50)
    marcas = models.CharField(max_length=50)
    valor_dolares = models.DecimalField(max_digits=10, decimal_places=2, null = True)
    descripcion = models.TextField(max_length=400, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True, null=True, editable=False)
    contacto_nombre = models.CharField(max_length=50, null=True, blank=True)
    contacto_email = models.EmailField(max_length=254, null=True, blank=True)
    contacto_telefono = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.marcas}, {self.modelos}"

    class Meta:
        verbose_name = "Ver Vehículo"
        verbose_name_plural = "Ver Vehículos"