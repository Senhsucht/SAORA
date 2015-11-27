from django.db import models
from SAORA.apps.Usuarios.models import *
from SAORA.apps.Evento.models import *

# Create your models here.

class Producto(models.Model):
	nombre = models.CharField(max_length=25)
	marca = models.CharField(max_length=25)
	cneto = models.CharField(max_length=15)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s : %s"%(self.nombre,self.marca)

class Inventario(models.Model):
	id_producto = models.ForeignKey('Producto')
	cantidad = models.PositiveIntegerField()
	descr = models.CharField(max_length=100)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s : %d"%(self.id_producto,self.cantidad)

class Donante(models.Model):
	nombre = models.CharField(max_length=25)
	ape_pat = models.CharField(max_length=25)
	ape_mat = models.CharField(max_length=25)
	rfc  = models.CharField(max_length=13)
	tel = models.IntegerField()
	direccion  = models.CharField(max_length=100)
	email = models.CharField(max_length=45)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s %s %s"%(self.nombre,self.ape_pat,self.ape_mat)

class Inv_Hist(models.Model):
	id_afiliado= models.ForeignKey('Usuarios.Afiliado')
	id_producto= models.ForeignKey('Producto')
	cantidad = models.PositiveIntegerField()
	descr  = models.CharField(max_length=100, null=True)
	# caducidad = models.IntegerField()
	id_donante = models.ForeignKey('Donante', null=True)
	id_evento = models.ForeignKey('Evento.Evento', null=True)
	alta_baja = models.BooleanField()
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s : %d : %s"%(self.id_producto,self.cantidad,self.alta_baja)
