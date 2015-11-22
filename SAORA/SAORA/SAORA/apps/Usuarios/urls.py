from django.conf.urls import include, patterns, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
	url(r'^alta_afil/',Alta_Afil,name='Alta_Afil'),
	url(r'^con_afil/',Con_Afil,name='Con_Afil'),
	url(r'^alta_usr/',Alta_Usr,name='Alta_Usr'),
	url(r'^con_usr/',Con_Usr,name='Con_Usr'),
	url(r'^alta_tusr/',Alta_tusr,name='Alta_tusr'),
	url(r'^con_tusr/',Con_tusr,name='Con_tusr'),
	url(r'^alta_tafil/',Alta_tafil,name='Alta_tafil'),
	url(r'^con_tafil/',Con_tafil,name='Con_tafil'),
	)
