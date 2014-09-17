from django.conf.urls import patterns, url

from gestion import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^listar/$', views.listar, name='listar'),
    url(r'^listar/(?P<message>\w+)/$', views.listar,name='listar1'),
    url(r'^save/$',views.save, name='save'), 
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),  
    url(r'^add/$', views.edit, name='add'),   
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),    
)