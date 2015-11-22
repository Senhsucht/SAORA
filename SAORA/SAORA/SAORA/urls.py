"""SAORA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from SAORA import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', include('SAORA.apps.Usuarios.urls')),
    url(r'^usr/', include('SAORA.apps.Usuarios.urls')),

    url(r'^$', include('SAORA.apps.Evento.urls')),
    url(r'^eve/', include('SAORA.apps.Evento.urls')),

    url(r'^$', include('SAORA.apps.Rescate.urls')),
    url(r'^res/', include('SAORA.apps.Rescate.urls')),

    url(r'^$', include('SAORA.apps.Inventario.urls')),
    url(r'^inv/', include('SAORA.apps.Inventario.urls')),

    url(r'^$', include('SAORA.apps.Adopcion.urls')),
    url(r'^adop/', include('SAORA.apps.Adopcion.urls')),

    url(r'media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),

]
