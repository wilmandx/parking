from django.contrib import admin

# Register your models here.

# Register your models here.
from gestion.models import *

class ValorTipoAdmin(admin.ModelAdmin):
    list_display = ('id','padre','nombre', 'activo')
    list_filter = ('padre','activo')
    search_fields=('nombre',)

class TarifaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'horas','valor')
    list_per_page=5

admin.site.register(Tarifa,TarifaAdmin)
admin.site.register(ValorTipo,ValorTipoAdmin)