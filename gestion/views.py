from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from gestion.models import Tarifa

# Create your views here.

@login_required
def index(request):
	usuario=request.user
	return HttpResponse(str(usuario.groups.values_list('name',flat=True))+"Hello,,,, world. You're at the polls index.")

def listar(request):
    list_tarifas=Tarifa.objects.all()
    context = {'site_title': 'Mi titulo','site_header':'prueball','tarifas_list':list_tarifas}
    return render(request, 'listar.html',context)