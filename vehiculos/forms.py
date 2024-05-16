from django import forms
from . import models


class lista_vehiculosform(forms.ModelForm):
    class Meta: 
        model = models.Ver_vehiculos
        fields = ["tipo","marcas","modelos"]