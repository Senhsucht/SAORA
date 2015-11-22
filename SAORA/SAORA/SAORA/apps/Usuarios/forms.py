from django import forms
from .models import *

class Form_Afil(forms.Form):
	Nombre = forms.CharField(max_length=15)
	Apellido_Paterno = forms.CharField(max_length=15)
	Apellido_Materno = forms.CharField(max_length=15)
	Edad = forms.IntegerField()
	Direccion  = forms.CharField(max_length=70)
	Tipo_de_Afiliado = forms.ModelChoiceField(queryset=Tafil.objects.all())
	Imagen = forms.ImageField(label='Selecciona un archivo')
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	# class Meta:
	#     model = Afiliado
	#     fields = '__all__'

class Form_Usr(forms.Form):
	Usuario = forms.CharField(max_length=15)
	Contrasena = forms.CharField(max_length=25)
	Afiliado = forms.ModelChoiceField(queryset=Afiliado.objects.all())
	Tipo_de_Usuario	= forms.ModelChoiceField(queryset=Tusr.objects.all())
	Activo = forms.BooleanField(widget=forms.HiddenInput(), required=False)

	# class Meta:
	# 	model = Usuario
	# 	fields = '__all__'

# class Select_Tafil(forms.Form):
# 	Tipo_de_Afil =  forms.ModelChoiceField(queryset=Tafil.objects.all())

 	# class Meta:
 	#     model = Tafil
 	#     fields = '__all__'

# class Select_Tusr(forms.Form):
# 	Tipo_de_Usuario =  forms.ModelChoiceField(queryset=Tusr.objects.all())

	# class Meta:
	#     model = Tusr
	#     fields = '__all__'

class Form_Tusr(forms.Form):
	Tipo_de_Usuario = forms.CharField(max_length=10)
	Descripcion = forms.CharField(max_length=50)

class Form_Tafil(forms.Form):
	Tipo_de_Afiliado = forms.CharField(max_length=10)
	Descripcion = forms.CharField(max_length=50)
