from django.contrib import admin
from django import forms

# Register your models here.

# Register your models here.
from gestion.models import *

class ValorTipoInline(admin.TabularInline):
    model = ValorTipo
    extra = 1

class ValorTipoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'activo')
    #list_filter = ('padre','activo')
    search_fields=('nombre',)
    exclude = ('padre','activo')
    inlines = [ValorTipoInline]
    list_display_links = ('id','nombre')
    def get_queryset(self, request):
        qs = super(ValorTipoAdmin, self).get_queryset(request)
        return qs.filter(padre=None)

class TarifaAdminForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(TarifaAdminForm, self).__init__(*args, **kwargs)
		# access object through self.instance...
		self.fields['tipoVehiculo'].queryset = ValorTipo.objects.filter(padre=1)

class TarifaAdmin(admin.ModelAdmin):
	form = TarifaAdminForm
	list_display = ('nombre','tipoVehiculo','horas','valor')
	list_per_page=5

class ConstanteAdmin(admin.ModelAdmin):
    list_display = ('nombre','valor')
        

admin.site.register(Tarifa,TarifaAdmin)
admin.site.register(ValorTipo,ValorTipoAdmin)
admin.site.register(Constante,ConstanteAdmin)