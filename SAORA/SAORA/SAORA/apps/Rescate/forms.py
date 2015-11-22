from django import forms
from SAORA.apps.Usuarios.models import *
from .models import *

class Form_Animal(forms.Form):
	Nombre = forms.CharField(max_length=20)
	Raza = forms.ModelChoiceField(queryset=Raza.objects.all())
	Edad = forms.IntegerField()
	Imagen = forms.ImageField(label='Selecciona un archivo')
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

class Form_Tanimal(forms.Form):
	Tipo_de_Animal = forms.CharField(max_length=20)
	Descripcion = forms.CharField(max_length=50)

class Form_Raza(forms.Form):
	Raza = forms.CharField(max_length=20)
	Descripcion = forms.CharField(max_length=50)
	Tipo_de_Animal = forms.ModelChoiceField(queryset=Tanimal.objects.all())

class Form_Rescate(forms.Form):
	Folio = forms.IntegerField()
	Afiliado = forms.ModelChoiceField(queryset=Afiliado.objects.all())
	Animal = forms.ModelChoiceField(queryset=Animal.objects.all())
	Lugar = forms.CharField(max_length=50)
