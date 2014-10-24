from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from gestion.models import ValorTipo,Parqueo,Tarifa
from django.forms import ModelForm
from django.http import HttpResponseRedirect
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.
class TarifaForm(ModelForm):
    class Meta:
        model = Tarifa
        fields = ['id', 'nombre' ,'horas']
        #fields = '__all__'

# Create your views here.
class ParqueoForm(ModelForm):
    class Meta:
        model = Parqueo
        fields = ['id','placa' ,'tipoVehiculo' ,'tipoTarifa']
        #fields = '__all__'

@login_required
def index(request):
	usuario=request.user
	return HttpResponse(str(usuario.groups.values_list('name',flat=True))+"Hello,,,, world. You're at the polls index.")

@login_required
def listar(request,message=None):
    list_tarifas=Tarifa.objects.all()
    if message:
    	message='Operacion realizada correctamente!!'
    context = {'message':message ,'tarifas_list':list_tarifas}
    return render(request, 'listar.html',context)

@login_required
def listar2(request,message=None):
    list_usuarios=User.objects.all()
    #if message:
    #	message='Operacion realizada correctamente!!'
    context = {'message':message ,'list_usuarios':list_usuarios}
    return render(request, 'listar2.html',context)

@login_required
def edit(request,id=None):
	if(id):
		tarifa=Tarifa.objects.get(id=id)
	else:
		tarifa=Tarifa()
	form = TarifaForm(instance=tarifa)
	return render(request,'add.html',{'tarifa':tarifa,'form':form})

@login_required
def save(request):
	ta,vt=Tarifa(),ValorTipo()
	vt.id,ta.tipoTarifa=1,vt
	if request.POST['id']!='':
		ta.id=int(request.POST['id'])
	form = TarifaForm(request.POST,instance=ta)
	if form.is_valid():
		form.save()
	return redirect('gestion:listar1',message='ok')

@login_required
def delete(request,id):
	Tarifa.objects.get(id=id).delete()
	return redirect('gestion:listar1',message='ok')

@login_required
def entradas(request):
	entrada=True
	context = {'opcion':'gestion:validar_entrada','entrada':entrada}
	return render(request, 'entradas.html',context)

@login_required
def validar_entrada(request):
	ta,vt,parqueo=Tarifa(),ValorTipo(),Parqueo()
	vt.id,ta.tipoTarifa=1,vt
	entrada=True
	if request.POST['placa']!='': 
		placa=request.POST['placa']
	#Buscar con la placa...si ya hay una entrada
	try:
		parqueo=Parqueo.objects.get(placa=placa,horaSalida=None)
		parqueo.horaSalida=timezone.now()
		diferencia=parqueo.horaSalida-parqueo.horaEntrada
		parqueo.horas=int(diferencia.seconds/60/60)+int(diferencia.days*24)
		parqueo.valor=5000
		entrada=False
	except Parqueo.DoesNotExist:
		parqueo.placa=placa
	context = {'opcion':'gestion:save_entrada','parqueo':parqueo,'entrada':entrada}
	return render(request, 'entradas.html',context)

@login_required
def save_entrada(request):
	entrada=True
	ta,vt,parqueo=Tarifa(),ValorTipo(),Parqueo()
	vt.id,ta.tipoTarifa=1,vt
	placa=''
	if request.POST['id']!='':
		parqueo.id=int(request.POST['id'])
	if request.POST['placa']!='':
		placa=request.POST['placa']
	#Buscar con la placa...si ya hay una entrada
	form = ParqueoForm(request.POST,instance=parqueo)
	list_parqueos=Parqueo.objects.all()
	context = {'list_parqueos':list_parqueos,'entrada':entrada}
	if form.is_valid():
		form.save()
	return render(request, 'entradas.html',context)

@login_required
def reportediario(request):
	list_parqueos=Parqueo.objects.all()
	context = {'list_parqueos':list_parqueos}
	return render(request, 'reportediario.html',context)