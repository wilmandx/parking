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
    if message:
    	message='Operacion realizada correctamente!!'
    datos = {'message':message ,'list_parametros':list_parametros}
    return render(request, 'parametros/listar.html',datos)

@login_required
def load(request):
    return render(request, 'parametros/load.html')