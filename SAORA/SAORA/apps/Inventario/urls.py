from django.conf.urls import include, patterns, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
	url(r'^alta_inv/',Alta_Inventario,name='Alta_Inventario'),
	url(r'^con_inv/',Con_Inventario,name='Con_Inventario'),
	url(r'^con_inv_edo/',Con_Inv_Estado,name='Con_Inv_Estado'),
	url(r'^baja_inv/',Baja_Inventario,name='Baja_Inventario'),
	url(r'^alta_prod/',Alta_Producto,name='Alta_Producto'),
	url(r'^con_prod/',Con_Producto,name='Con_Producto'),
	url(r'^alta_donante/',Alta_Donante,name='Alta_Donante'),
	url(r'^con_donante/',Con_Donante,name='Con_Donante'),
	)
