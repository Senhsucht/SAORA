from django.db import models
from SAORA.apps.Usuarios.models import *
from django.template.defaultfilters import slugify


# Create your models here.

class Tanimal(models.Model):
	tanimal = models.CharField(max_length=25,unique=True)
	descr = models.CharField(max_length=100)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s : %s"%(self.tanimal,self.descr)

class Raza(models.Model):
	raza = models.CharField(max_length=25,unique=True)
	descr = models.CharField(max_length=100)
	id_tanimal = models.ForeignKey('Tanimal')
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s : %s"%(self.raza,self.descr)

class Animal(models.Model):
	nombre = models.CharField(max_length=25)
	id_raza = models.ForeignKey('Raza')
	edad = models.IntegerField()
	ult_act = models.DateField(auto_now_add=True)
	imagen = models.ImageField(upload_to='animales/')

	SLUG = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
	    self.SLUG = slugify(self.imagen)
	    super(Animal, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s : Edad %d"%(self.nombre,self.edad)

class Rescate(models.Model):
	folio = models.IntegerField(unique=True)
	id_afil = models.ForeignKey('Usuarios.Afiliado')
	id_animal = models.ForeignKey('Animal')
	lugar = models.CharField(max_length=100)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "No. Rescate: %d"%(self.folio)
