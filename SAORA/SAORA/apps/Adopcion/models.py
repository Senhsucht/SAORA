from django.db import models
from SAORA.apps.Rescate.models import *

# Create your models here.

class Ado_Edo(models.Model):
	estado = models.CharField(max_length=10,unique=True)
	descr = models.CharField(max_length=50)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s"%(self.estado)

class Adoptante(models.Model):
	nombre = models.CharField(max_length=15)
	ape_pat = models.CharField(max_length=15)
	ape_mat = models.CharField(max_length=15)
	edad = models.IntegerField()
	direccion  = models.CharField(max_length=70)
	tel = models.IntegerField()
	email = models.CharField(max_length=35)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s %s %s"%(self.nombre,self.ape_pat,self.ape_mat)

class Adopcion(models.Model):
	folio = models.IntegerField(unique=True)
	id_adoptante = models.ForeignKey('Adoptante')
	id_animal = models.ForeignKey('Rescate.Animal')
	id_ado_edo = models.ForeignKey('Ado_Edo')
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "No Adopcion: %d"%(self.folio)

class Visita(models.Model):
	id_adopcion = models.ForeignKey('Adopcion')
	no_visita = models.IntegerField()
	descr = models.CharField(max_length=50)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "Adopcion: %s, No Visita: %d"%(self.id_adopcion,self.no_visita)
