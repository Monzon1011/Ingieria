from django.conf.urls import patterns, include, url

from django.contrib import admin

from Aplicacion import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Compra/',views.Compra_list),
    url(r'^Persona/',views.Persona_list),
    url(r'^Producto/',views.Producto_list),

)
