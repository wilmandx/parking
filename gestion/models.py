from django.db import models

# Create your models here.
class ValorTipo(models.Model):
	nombre = models.CharField(max_length=500)
	descripcion = models.CharField(max_length=3000)
	padre = models.ForeignKey('self',blank=True, null=True,)
	activo = models.BooleanField(default=True)
	def __str__(self):
		return self.nombre
	
class Tarifa(models.Model):
	nombre = models.CharField(max_length=200)
	horas = models.IntegerField(default=0)
	valor = models.FloatField(default=0)
	tipoVehiculo = models.ForeignKey(ValorTipo)
	def __str__(self):
		return self.nombre

class Parqueo(models.Model):
	placa = models.CharField(max_length=20)
	horaEntrada = models.DateTimeField(auto_now=True)
	horaSalida = models.DateTimeField(auto_now=False,blank=True, null=True)
	tipoVehiculo = models.ForeignKey(ValorTipo,related_name='+')
	tipoTarifa = models.ForeignKey(ValorTipo,related_name='+')
	nroFactura = models.IntegerField(blank=True, null=True)
	nroRecibo = models.IntegerField(blank=True, null=True)
	horas = models.IntegerField(blank=True, null=True)
	valor = models.FloatField(blank=True, null=True)
	def __str__(self):
		return self.placa