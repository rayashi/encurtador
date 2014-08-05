from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'encurtador_app.views.index'),
    url(r'encurtar', 'encurtador_app.views.encurtar'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<link>\w+)$', 'encurtador_app.views.linkar'),
)
