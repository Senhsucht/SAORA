from django.conf.urls import include, patterns, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
	url(r'^alta_adoptante/',Alta_Adoptante,name='Alta_Adoptante'),

	)
