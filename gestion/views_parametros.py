from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from gestion.models import *
from django.forms import ModelForm
from django.http import HttpResponseRedirect
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

@login_required
def index(request):
	usuario=request.user
	return HttpResponse(str(usuario.groups.values_list('name',flat=True))+"Hello,,,, world. You're at the polls index.")

@login_required
def listar(request,message=None):
    list_parametros=Constante.objects.all()
    if message=='c01':
    	message='Operacion realizada correctamente!!'
    elif message=='c02':
    	message='Nombre de parametro invalido'
    elif message=='c03':
    	message='Ya existe el parametro'
    datos = {'message_success':message ,'list_parametros':list_parametros}
    return render(request, 'parametros/listar.html',datos)

@login_required
def load(request,idParametro=None):
	#print("llego el id para modificar="+idParametro)
	constante1=Constante()
	datos={}
	if idParametro!=None:
		constante1=Constante.objects.get(id=idParametro)
	datos['parametro']=constante1
	return render(request, 'parametros/load.html',datos)

@login_required
def guardar(request):
	codigo='c01'
	listIguales=Constante.objects.filter(nombre=request.POST['nombre'])
	constante=Constante()
	if request.POST['id']!='':
		print("llego el id")
		constante.id=request.POST['id']
	else:
		print("no llego el id")
	print("nombre="+request.POST['nombre'])
	print("valor="+request.POST['valor'])
	print("descripcion="+request.POST['descripcion'])
	constante.nombre=request.POST['nombre']
	constante.valor=request.POST['valor']
	constante.descripcion=request.POST['descripcion']
	if request.POST['nombre']=='HORAS':
		codigo='c02'
	elif len(listIguales)>0:
		codigo='c03'
	else:
		constante.save()
	return redirect('gestion:listarParametros',message=codigo)

@login_required
def eliminar(request,idParametro):
	constante1=Constante.objects.get(id=idParametro)
	constante1.delete()
	print("parametro que llega="+idParametro)
	return redirect('gestion:listarParametros')