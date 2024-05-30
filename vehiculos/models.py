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


class Precio(models.Model):
    valor_dolares = models.DecimalField(max_digits=10, decimal_places=2, null= True)

    def __str__(self):
        return f"${self.valor_dolares}"

    class Meta:
        verbose_name = "Precio"
        verbose_name_plural = "Precios"


class Descripcion(models.Model):
    descripcion = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Estado del Vehículo"
        verbose_name_plural = "Estados de los Vehículos"


class Ver_vehiculos(models.Model):
    tipo = models.CharField(max_length=30)
    modelos = models.CharField(max_length=30)
    marcas = models.CharField(max_length=30)
    valor_dolares = models.DecimalField(max_digits=10, decimal_places=2, null = True)
    descripcion = models.CharField(max_length=400, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True, null=True, editable=False)
    # fecha_actualizacion = models.DateField(null=True, blank=True, editable=False, default=timezone.now)

    def __str__(self) -> str:
        return f"{self.marcas}, {self.modelos}"

    class Meta:
        verbose_name = "Ver Vehículo"
        verbose_name_plural = "Ver Vehículos"