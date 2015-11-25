from django.conf.urls import include, patterns, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
	url(r'^alta_animal/',Alta_Animal,name='Alta_Animal'),
	url(r'^con_animal/',Con_Animal,name='Con_Animal'),
	url(r'^alta_tanimal/',Alta_tanimal,name='Alta_tanimal'),
	url(r'^con_tanimal/',Con_tanimal,name='Con_tanimal'),
	url(r'^alta_raza/',Alta_Raza,name='Alta_Raza'),
	url(r'^con_raza/',Con_Raza,name='Con_Raza'),
	url(r'^alta_rescate/',Alta_Rescate,name='Alta_Rescate'),
	url(r'^con_rescate/',Con_Rescate,name='Con_Rescate'),
	)
