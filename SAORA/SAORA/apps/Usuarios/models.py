from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

# class Tusr(models.Model):
# 	tusr = models.CharField(max_length=10,unique=True)
# 	descr = models.CharField(max_length=50)
# 	ult_act = models.DateField(auto_now_add=True)
# 
# 	def __unicode__(self):
# 		return "%s : %s"%(self.tusr,self.descr)

class Tafil(models.Model):
	tafil = models.CharField(max_length=10,unique=True)
	descr = models.CharField(max_length=50)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s : %s"%(self.tafil,self.descr)

class Afiliado(models.Model):
	nombre = models.CharField(max_length=15)
	ape_pat = models.CharField(max_length=15)
	ape_mat = models.CharField(max_length=15)
	edad = models.PositiveIntegerField()
	direccion  = models.CharField(max_length=70)
	tel = models.PositiveIntegerField()
	email = models.CharField(max_length=35)
	id_tafil = models.ForeignKey('Tafil')
	ult_act = models.DateField(auto_now_add=True)
	imagen = models.ImageField(upload_to='afiliados/')

	SLUG = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
	    self.SLUG = slugify(self.imagen)
	    super(Afiliado, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s %s"%(self.nombre,self.ape_pat,self.ape_mat)

class Usuario(models.Model):
	user = models.OneToOneField(User, unique=True)
	id_afil = models.ForeignKey('Afiliado')
	activo = models.BooleanField(default=True)
	ult_act = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "Usuario: %s"%(self.user)
