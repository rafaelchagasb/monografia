#from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.defaults import * 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monografia.views.home', name='home'),
    # url(r'^monografia/', include('monografia.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # Uncomment the next line to enable the admin:
	url(r'^$', 'map.views.home', name='home'),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^map/', include('map.urls')),
)
