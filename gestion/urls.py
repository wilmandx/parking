from django.conf.urls import patterns, url

from gestion import views,views_parametros

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^listar/$', views.listar, name='listar'),
    url(r'^listar2/$', views.listar2, name='listar2'),
    url(r'^listar/(?P<message>\w+)/$', views.listar,name='listar1'),
    url(r'^save/$',views.save, name='save'), 
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),  
    url(r'^add/$', views.edit, name='add'),   
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^entradas/$', views.entradas, name='entradas'),
    url(r'^entradas/save/$', views.save_entrada, name='save_entrada'),
    url(r'^entradas/validar/$', views.validar_entrada, name='validar_entrada'),
    url(r'^reportediario/$', views.reportediario, name='reportediario'),
    url(r'^parametros/$', views_parametros.listar, name='listarParametros'),
    url(r'^parametros/(?P<message>\w+)/$', views_parametros.listar, name='listarParametros'),
    url(r'^loadparametro/$', views_parametros.load, name='loadParametros'),
    url(r'^loadparametro/(?P<idParametro>\d+)/$', views_parametros.load, name='loadParametros'),
    url(r'^guardaparametro/$', views_parametros.guardar, name='guardarParametros'),
    url(r'^eliminarParametro/(?P<idParametro>\d+)/$', views_parametros.eliminar, name='eliminarParametros'),
)