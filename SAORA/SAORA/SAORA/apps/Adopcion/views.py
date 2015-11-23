from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def Alta_Adoptante(request):
    form = Form_Adoptante()
    ctx={'mensaje':'Ingrese datos','form':form}

    if request.method=='POST':
        form = Form_Adoptante(request.POST,request.FILES)

        if form.is_valid():
            a = Adoptante()

            a.nombre = form.cleaned_data['Nombre']
            a.ape_pat = form.cleaned_data['Apellido_Paterno']
            a.ape_mat = form.cleaned_data['Apellido_Materno']
            a.edad = form.cleaned_data['Edad']
            a.direccion = form.cleaned_data['Direccion']
            a.tel = form.cleaned_data['Telefono']
            a.email = form.cleaned_data['Email']

            a.save()

            form = Form_Adoptante()
            ctx={'mensaje': 'Adoptante guardado con exito!','form':form}

        else:

            ctx={'mensaje': 'Error en los datos.','form':form}

    return render(request,'Adopcion/alta_adoptante.html',ctx)

def Con_Adoptante(request):
	obj = Adoptante.objects.all()
	ctx = {'mensaje':obj}

	return render(request,'Adopcion/con_adoptante.html',ctx)

def Alta_Ado_Edo(request):
    form = Form_Ado_Edo()
    ctx={'mensaje':'Ingrese datos','form':form}

    if request.method=='POST':
        form = Form_Ado_Edo(request.POST,request.FILES)

        if form.is_valid():
            a = Ado_Edo()

            a.estado = form.cleaned_data['Estado']
            a.descr = form.cleaned_data['Descripcion']

            a.save()

            form = Form_Ado_Edo()
            ctx={'mensaje': 'Adoptante guardado con exito!','form':form}

        else:
            ctx={'mensaje': 'Error en los datos.','form':form}

    return render(request,'Adopcion/alta_ado_edo.html',ctx)

def Con_Ado_Edo(request):
	obj = Ado_Edo.objects.all()
	ctx = {'mensaje':obj}

	return render(request,'Adopcion/con_ado_edo.html',ctx)

def Alta_Adopcion(request):
    form = Form_Adopcion()
    ctx={'mensaje':'Ingrese datos','form':form}

    if request.method=='POST':
        form = Form_Adopcion(request.POST,request.FILES)

        if form.is_valid():
            a = Adopcion()

            a.folio = form.cleaned_data['Folio']
            a.id_adoptante = form.cleaned_data['Adoptante']
            a.id_animal = form.cleaned_data['Animal']
            a.id_ado_edo = form.cleaned_data['Estado']

            a.save()

            form = Form_Adopcion()
            ctx={'mensaje': 'Adopcion guardado con exito!','form':form}

        else:
            ctx={'mensaje': 'Error en los datos.','form':form}

    return render(request,'Adopcion/alta_adopcion.html',ctx)

def Con_Adopcion(request):
	obj = Adopcion.objects.all()
	ctx = {'mensaje':obj}

	return render(request,'Adopcion/con_adopcion.html',ctx)

def Alta_Visita(request):
    form = Form_Visita()
    ctx={'mensaje':'Ingrese datos','form':form}

    if request.method=='POST':
        form = Form_Visita(request.POST,request.FILES)

        if form.is_valid():
            a = Adopcion()

            a.id_adopcion = form.cleaned_data['Adopcion']
            a.no_visita = form.cleaned_data['No_de_Visita']
            a.descr = form.cleaned_data['Descripcion']

            a.save()

            form = Form_Visita()
            ctx={'mensaje': 'Visita guardado con exito!','form':form}

        else:
            ctx={'mensaje': 'Error en los datos.','form':form}

    return render(request,'Adopcion/alta_visita.html',ctx)

def Con_Visita(request):
	obj = Visita.objects.all()
	ctx = {'mensaje':obj}

	return render(request,'Adopcion/con_visita.html',ctx)
