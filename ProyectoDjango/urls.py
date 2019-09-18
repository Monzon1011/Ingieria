from django.conf.urls import patterns, include, url
from Aplicacion import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Compra/', include(Aplicacion.urls.Compra_list)),
    url(r'^Persona/', urls.Persona_List),
    url(r'^Producto/', urls.Producto_list),

)
