from django.contrib import admin

from .models import Item,Movimiento

# Register your models here.

admin.site.site_header = "FABS INVENTARIO"
admin.site.site_title = "FABS INVENTARIO"

class MovimientoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cantidad de items', {
            'fields': ('item','cantidad')
        }),
        ('Tipo y fecha de movimiento', {
            'fields': ('fecha','movimiento','bodega')
        }),        
    ) 

admin.site.register(Item)
admin.site.register(Movimiento, MovimientoAdmin)