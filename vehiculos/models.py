from django.db import models

class Tipo(models.Model):
    tipo = models.CharField(max_length= 55, unique=True)

    def __str__(self) -> str:
        return self.tipo
    
class Marcas(models.Model):
    marca = models.CharField(max_length= 55)

    def __str__(self) -> str:
        return self.marca

class Modelos(models.Model):
    modelo = models.CharField(max_length= 55, unique=True)

    def __str__(self) -> str:
        return self.modelo
     
class Ver_vehiculos(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True, blank=True)    
    modelos = models.ForeignKey(Modelos, on_delete=models.SET_NULL, null=True, blank=True)
    marcas = models.ForeignKey(Marcas, on_delete=models.SET_NULL, null=True, blank=True)