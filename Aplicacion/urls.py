from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Compra/', 'Aplcacion.urls.Compra_list'),
    url(r'^Persona/', 'Aplcacion.urls.Persona_List'),
    url(r'^Producto/', 'Aplcacion.urls.Producto_list'),

)
