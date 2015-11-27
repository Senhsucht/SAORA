from django.db import models
from SAORA.apps.Usuarios.models import *

# Create your models here.

class Eve_Edo(models.Model):
	eve_edo = models.CharField(max_length=25,unique=True)
	descr = models.CharField(max_length=100)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s : %s"%(self.eve_edo,self.descr)

class Tevento(models.Model):
	tevento = models.CharField(max_length=25,unique=True)
	descr = models.CharField(max_length=100)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s : %s"%(self.tevento,self.descr)

class Patrocinador(models.Model):
	nombre = models.CharField(max_length=25)
	ape_pat = models.CharField(max_length=25)
	ape_mat = models.CharField(max_length=25)
	rfc  = models.CharField(max_length=13)
	tel = models.IntegerField()
	email = models.CharField(max_length=45)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s %s %s"%(self.nombre,self.ape_pat,self.ape_mat)

class Evento(models.Model):
	nombre = models.CharField(max_length=50)
	descr = models.CharField(max_length=100)
	lugar = models.CharField(max_length=50)
	fecha = models.DateTimeField()
	id_tevento = models.ForeignKey('Tevento')
	id_eve_edo = models.ForeignKey('Eve_Edo')
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s"%(self.nombre)

class Eve_Patro(models.Model):
	id_evento = models.ForeignKey('Evento')
	id_patrocinador = models.ForeignKey('Patrocinador')
	descr = models.CharField(max_length=100)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%d"%(self.id)

# class Eve_Asist(models.Model):
# 	id_evento = models.ForeignKey('Evento')
# 	id_afil = models.ForeignKey('Usuarios.Afiliado')
# 	hora_llagada = models.TimeField()
# 	hora_salida = models.TimeField()
# 	ult_act = models.DateField(auto_now_add=True)
#
# 	def __unicode__(self):
# 		return "%d"%(self.id)
