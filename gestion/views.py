from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from gestion.models import Tarifa
from django.forms import ModelForm

# Create your views here.
class TarifaForm(ModelForm):
    class Meta:
        model = Tarifa
        fields = ['id', 'nombre', 'dias','horas']
        #fields = '__all__'

@login_required
def index(request):
	usuario=request.user
	return HttpResponse(str(usuario.groups.values_list('name',flat=True))+"Hello,,,, world. You're at the polls index.")

def listar(request):
    list_tarifas=Tarifa.objects.all()
    context = {'site_title': 'Mi titulo','site_header':'prueball','tarifas_list':list_tarifas}
    return render(request, 'listar.html',context)

def add(request):
	return render(request,'add.html')

def edit(request,id):
	tarifa=Tarifa.objects.get(id=id)
	return render(request,'add.html',{'tarifa':tarifa})

def save(request):
	#if request.POST['id']!='':
	#
	#else
	ta=Tarifa()
	if request.POST['id']!='':
		ta.id=int(request.POST['id'])
		print("id encontrado="+request.POST['id'])
	form = TarifaForm(request.POST,instance=ta)
	if form.is_valid():
		print("guardo")
		print(form)
		form.save()

	list_tarifas=Tarifa.objects.all()
	context = {'message': 'Registro guardado','tarifas_list':list_tarifas}
	return render(request,'listar.html',context)

def delete(request,id):
	Tarifa.objects.get(id=id).delete()
	list_tarifas=Tarifa.objects.all()
	context = {'message': 'Registro eliminado','tarifas_list':list_tarifas}
	return render(request, 'listar.html',context)