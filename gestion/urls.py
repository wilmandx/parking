from django.conf.urls import patterns, url

from gestion import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)