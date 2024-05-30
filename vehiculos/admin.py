from django.contrib import admin
from .models import Ver_vehiculos, Marcas, Modelos, Tipo, Descripcion, Precio

class VehiculosAdmin(admin.ModelAdmin):
    
    list_display = (
        "marcas", "modelos",
        "tipo", "fecha_creacion",
        "valor_dolares"
        )
    list_display_links = ()
    list_filter = ("marcas",)
    date_hierarchy = "fecha_creacion"
    

admin.site.register(Ver_vehiculos, VehiculosAdmin)
admin.site.register(Marcas)
admin.site.register(Modelos)
admin.site.register(Tipo)
admin.site.register(Precio)
admin.site.register(Descripcion)