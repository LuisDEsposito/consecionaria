from django.db import models


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
    tipo = models.ManyToManyField(Tipo)
    modelos = models.ManyToManyField(Modelos)
    marcas = models.ManyToManyField(Marcas)

    class Meta:
        verbose_name = "Ver Vehículo"
        verbose_name_plural = "Ver Vehículos"