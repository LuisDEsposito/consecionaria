from django.contrib import admin

from . import models

admin.site.register(models.Ver_vehiculos)
admin.site.register(models.Marcas)
admin.site.register(models.Modelos)
admin.site.register(models.Tipo)
admin.site.register(models.Precio)
admin.site.register(models.Descripcion)