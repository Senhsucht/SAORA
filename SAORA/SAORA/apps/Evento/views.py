from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def Alta_Eve_Edo(request):
    form = Form_Eve_Edo()
    ctx={'mensaje': 'Ingrese datos de nuevo estado de evento','form':form}

    if request.method == 'POST':
        form = Form_Eve_Edo(request.POST,request.FILES)

        if form.is_valid():
            t= Eve_Edo()

            t.eve_edo = form.cleaned_data['Estado_de_Evento']
            t.descr = form.cleaned_data['Descripcion']

            t.save()
            form = Form_Eve_Edo()

            ctx={'mensaje':'Registro exitoso!','form':form}
        else:
            ctx={'mensaje':'Error en los datos.','form':form}

    return render(request,'Evento/alta_eveedo.html',ctx)

def Con_Eve_Edo(request):
    obj = Eve_Edo.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Evento/con_eveedo.html',ctx)

def Alta_teve(request):
    form = Form_Tevento()
    ctx={'mensaje': 'Ingrese datos de nuevo tipo de evento','form':form}

    if request.method == 'POST':
        form = Form_Tevento(request.POST,request.FILES)

        if form.is_valid():
            t= Tevento()

            t.tevento = form.cleaned_data['Tipo_de_Evento']
            t.descr = form.cleaned_data['Descripcion']

            t.save()
            form = Form_Tevento()

            ctx={'mensaje':'Registro exitoso!','form':form}
        else:
            ctx={'mensaje':'Error en los datos.','form':form}

    return render(request,'Evento/alta_teve.html',ctx)

def Con_teve(request):
    obj = Tevento.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Evento/con_teve.html',ctx)

def Alta_Eve_Patro(request):
    form = Form_Eve_Patro()
    ctx={'mensaje': 'Ingrese datos de nuevo patrocinador de evento','form':form}

    if request.method == 'POST':
        form = Form_Eve_Patro(request.POST,request.FILES)

        if form.is_valid():
            t= Eve_Patro()

            t.id_evento = form.cleaned_data['Evento']
            t.id_patrocinador = form.cleaned_data['Patrocinador']
            t.descr = form.cleaned_data['Descripcion']

            t.save()
            form = Form_Eve_Patro()

            ctx={'mensaje':'Registro exitoso!','form':form}

        else:
            ctx={'mensaje':'Error en los datos.','form':form}

    return render(request,'Evento/alta_eve_patro.html',ctx)

def Con_Eve_Patro(request):
    obj = Eve_Patro.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Evento/con_eve_patro.html',ctx)

def Alta_Patrocinador(request):
    form = Form_Patrocinador()
    ctx={'mensaje': 'Ingrese datos de nuevo patrocinador','form':form}

    if request.method == 'POST':
        form = Form_Patrocinador(request.POST,request.FILES)

        if form.is_valid():
            t= Patrocinador()

            t.nombre = form.cleaned_data['Nombre']
            t.ape_pat = form.cleaned_data['Apellido_Paterno']
            t.ape_mat = form.cleaned_data['Apellido_Materno']
            t.rfc = form.cleaned_data['RFC']
            t.tel = form.cleaned_data['Telefono']
            t.email = form.cleaned_data['Email']

            t.save()
            form = Form_Patrocinador()

            ctx={'mensaje':'Registro exitoso!','form':form}

        else:
            ctx={'mensaje':'Error en los datos.','form':form}

    return render(request,'Evento/alta_patro.html',ctx)

def Con_Patrocinador(request):
    obj = Patrocinador.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Evento/con_patro.html',ctx)

def Alta_Evento(request):
    form = Form_Evento()
    ctx={'mensaje': 'Ingrese datos de nuevo evento','form':form}

    if request.method == 'POST':
        form = Form_Evento(request.POST,request.FILES)

        if form.is_valid():
            t= Evento()

            t.nombre = form.cleaned_data['Nombre']
            t.descr = form.cleaned_data['Descripcion']
            t.lugar = form.cleaned_data['Lugar']
            t.fecha = form.cleaned_data['Fecha_y_Hora']
            t.id_tevento = form.cleaned_data['Tipo_de_Evento']
            t.id_eve_edo = form.cleaned_data['Estado_de_Evento']

            t.save()
            form = Form_Evento()

            ctx={'mensaje':'Registro exitoso!','form':form}

        else:
            ctx={'mensaje':'Error en los datos.','form':form}

    return render(request,'Evento/alta_eve.html',ctx)

def Con_Evento(request):
    obj = Evento.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Evento/con_eve.html',ctx)
