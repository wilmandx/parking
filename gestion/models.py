from django.db import models

# Create your models here.
class ValorTipo(models.Model):
	nombre = models.CharField(max_length=1000)
	descripcion = models.CharField(max_length=3000)
	padre = models.ForeignKey('self',null=True)
	activo = models.BooleanField(default=True)
	
class Tarifa(models.Model):
	nombre = models.CharField(max_length=200)
	horas = models.IntegerField(default=0)
	dias = models.IntegerField(default=0)
	valor = models.FloatField(default=0)
	#tipoTarifa = models.ForeignKey(ValorTipo)