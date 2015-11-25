from django import forms
from .models import *

class Form_Eve_Edo(forms.Form):
    Estado_de_Evento = forms.CharField(max_length=10)
    Descripcion = forms.CharField(max_length=50)

class Form_Tevento(forms.Form):
    Tipo_de_Evento = forms.CharField(max_length=10)
    Descripcion = forms.CharField(max_length=50)

class Form_Patrocinador(forms.Form):
    Nombre = forms.CharField(max_length=15)
    Apellido_Paterno = forms.CharField(max_length=15)
    Apellido_Materno = forms.CharField(max_length=15)
    RFC = forms.CharField(max_length=13)
    Telefono  = forms.IntegerField()
    Email = forms.CharField(max_length=35)

class Form_Evento(forms.Form):
    Nombre = forms.CharField(max_length=25)
    Descripcion = forms.CharField(max_length=50)
    Lugar = forms.CharField(max_length=50)
    Fecha_y_Hora = forms.DateTimeField()
    Tipo_de_Evento = forms.ModelChoiceField(queryset=Tevento.objects.all())
    Estado_de_Evento = forms.ModelChoiceField(queryset=Eve_Edo.objects.all())

class Form_Eve_Patro(forms.Form):
    Evento = forms.ModelChoiceField(queryset=Evento.objects.all())
    Patrocinador = forms.ModelChoiceField(queryset=Patrocinador.objects.all())
    Descripcion = forms.CharField(max_length=50)
