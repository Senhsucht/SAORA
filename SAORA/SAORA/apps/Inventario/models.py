from django.db import models
from SAORA.apps.Usuarios.models import *
from SAORA.apps.Evento.models import *

# Create your models here.

class Producto(models.Model):
	nombre = models.CharField(max_length=15)
	marca = models.CharField(max_length=15)
	cneto = models.CharField(max_length=10)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s : %s"%(self.nombre,self.marca)

class Inventario(models.Model):
	id_producto = models.ForeignKey('Producto')
	cantidad = models.PositiveIntegerField()
	descr = models.CharField(max_length=50)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s : %d"%(self.id_producto,self.cantidad)

class Donante(models.Model):
	nombre = models.CharField(max_length=15)
	ape_pat = models.CharField(max_length=15)
	ape_mat = models.CharField(max_length=15)
	rfc  = models.CharField(max_length=13)
	tel = models.IntegerField()
	direccion  = models.CharField(max_length=70)
	email = models.CharField(max_length=35)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s %s %s"%(self.nombre,self.ape_pat,self.ape_mat)

class Inv_Hist(models.Model):
	id_afiliado= models.ForeignKey('Usuarios.Afiliado')
	id_producto= models.ForeignKey('Producto')
	cantidad = models.PositiveIntegerField()
	descr  = models.CharField(max_length=50, null=True)
	# caducidad = models.IntegerField()
	id_donante = models.ForeignKey('Donante', null=True)
	id_evento = models.ForeignKey('Evento.Evento', null=True)
	alta_baja = models.BooleanField()
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s : %d : %s"%(self.id_producto,self.cantidad,self.alta_baja)
