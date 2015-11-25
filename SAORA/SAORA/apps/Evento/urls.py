from django.conf.urls import include, patterns, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
	url(r'^alta_eve_patro/',Alta_Eve_Patro,name='Alta_Eve_Patro'),
	url(r'^con_eve_patro/',Con_Eve_Patro,name='Con_Eve_Patro'),
	url(r'^alta_eve/',Alta_Evento,name='Alta_Evento'),
	url(r'^con_eve/',Con_Evento,name='Con_Evento'),
	url(r'^alta_eveedo/',Alta_Eve_Edo,name='Alta_Eve_Edo'),
	url(r'^con_eveedo/',Con_Eve_Edo,name='Con_Eve_Edo'),
	url(r'^alta_patro/',Alta_Patrocinador,name='Alta_Patrocinador'),
	url(r'^con_patro/',Con_Patrocinador,name='Con_Patrocinador'),
	url(r'^alta_teve/',Alta_teve,name='Alta_teve'),
	url(r'^con_teve/',Con_teve,name='Con_teve'),

	)
