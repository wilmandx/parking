from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm

@login_required
def index(request):
	#usuario=request.user
	return render(request, 'base.html')
	#return HttpResponse(str(usuario.groups.values_list('name',flat=True))+"Hello,,,, world. You're at the polls index.")


@login_required
def index2(request):
	return render(request, 'base_layout.html')

@login_required
def forms(request):
	return render(request, 'forms.html')