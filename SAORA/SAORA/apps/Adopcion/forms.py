from django import forms
from .models import *
from SAORA.apps.Rescate.models import *

class Form_Adoptante(forms.Form):
	Nombre = forms.CharField(max_length=15)
	Apellido_Paterno = forms.CharField(max_length=15)
	Apellido_Materno = forms.CharField(max_length=15)
	Edad = forms.IntegerField(min_value=0)
	Direccion = forms.CharField(max_length=70)
	Telefono = forms.IntegerField()
	Email = forms.CharField(max_length=35)

class Form_Ado_Edo(forms.Form):
	Estado = forms.CharField(max_length=10)
	Descripcion = forms.CharField(max_length=50)

class Form_Adopcion(forms.Form):
	Folio = forms. IntegerField(min_value=0)
	Adoptante = forms.ModelChoiceField(queryset=Adoptante.objects.all())
	Animal = forms.ModelChoiceField(queryset=Animal.objects.all())
	Estado = forms.ModelChoiceField(queryset=Ado_Edo.objects.all())

class Form_Visita(forms.Form):
	Adopcion = forms.ModelChoiceField(queryset=Adopcion.objects.all())
	No_de_Visita = forms.IntegerField(min_value=0)
	Descripcion = forms.CharField(max_length=50)
