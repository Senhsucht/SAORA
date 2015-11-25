from django.conf.urls import include, patterns, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
	url(r'^alta_adoptante/',Alta_Adoptante,name='Alta_Adoptante'),
	url(r'^con_adoptante/',Con_Adoptante,name='Con_Adoptante'),
	url(r'^alta_ado_edo/',Alta_Ado_Edo,name='Alta_Ado_Edo'),
	url(r'^con_ado_edo/',Con_Ado_Edo,name='Con_Ado_Edo'),
	url(r'^alta_adopcion/',Alta_Adopcion,name='Alta_Adopcion'),
	url(r'^con_adopcion/',Con_Adopcion,name='Con_Adopcion'),
	url(r'^alta_visita/',Alta_Visita,name='Alta_Visita'),
	url(r'^con_visita/',Con_Visita,name='Con_Visita'),
	)
