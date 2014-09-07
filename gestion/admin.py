from django.contrib import admin

# Register your models here.

# Register your models here.
from gestion.models import *

class ValorTipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo')

admin.site.register(Tarifa)
admin.site.register(ValorTipo,ValorTipoAdmin)