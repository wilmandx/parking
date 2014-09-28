from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'parking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^gestion/', include('gestion.urls',namespace="gestion")),
    url(r'^parking/$', 'parking.views.index', name='home'),
    url(r'^parking2/$', 'parking.views.index2', name='home2'),
    url(r'^parking2/forms$', 'parking.views.forms', name='forms'),
)
