from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from gestion.models import Tarifa
from gestion.models import ValorTipo
from django.forms import ModelForm
from django.http import HttpResponseRedirect

# Create your views here.
class TarifaForm(ModelForm):
    class Meta:
        model = Tarifa
        fields = ['id', 'nombre' ,'horas']
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
	return render(request, 'entradas.html')