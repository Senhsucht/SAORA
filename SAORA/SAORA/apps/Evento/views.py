from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def Alta_Eve_Edo(request):
    # form = Form_Eve_Edo()
    ctx={'mensaje': 'Ingrese datos de nuevo estado de evento'}

    if request.POST:
        t= Eve_Edo()

        t.eve_edo = request.POST.get('estado')
        t.descr = request.POST.get('descr')

        t.save()
        # form = Form_Eve_Edo()

        ctx={'mensaje':'Registro exitoso!'}
    else:
        ctx={'mensaje':'Error en los datos.'}

    return render(request,'Evento/alta_eveedo.html',ctx)

@login_required(login_url='/')
def Con_Eve_Edo(request):
    obj = Eve_Edo.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Evento/con_eveedo.html',ctx)

@login_required(login_url='/')
def Alta_teve(request):
    # form = Form_Tevento()
    ctx={'mensaje': 'Ingrese datos de nuevo tipo de evento'}

    if request.POST:
        t= Tevento()

        t.tevento = request.POST.get('teve')
        t.descr = request.POST.get('descr')

        t.save()
        # form = Form_Tevento()

        ctx={'mensaje':'Registro exitoso!'}
    else:
        ctx={'mensaje':'Error en los datos.'}

    return render(request,'Evento/alta_teve.html',ctx)

@login_required(login_url='/')
def Con_teve(request):
    obj = Tevento.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Evento/con_teve.html',ctx)

@login_required(login_url='/')
def Alta_Eve_Patro(request):
    # form = Form_Eve_Patro()
    evento = Evento.objects.all()
    patrocinador = Patrocinador.objects.all()

    ctx={'mensaje': 'Ingrese datos de nuevo patrocinador de evento','evento':evento,'patrocinador':patrocinador}

    if request.POST:
        t= Eve_Patro()

        patro = Patrocinador.objects.get(id=request.POST.get('patro'))
        eve = Evento.objects.get(id=request.POST.get('eve'))

        t.id_evento = eve
        t.id_patrocinador = patro
        t.descr = request.POST.get('descr')

        t.save()
        # form = Form_Eve_Patro()

        ctx={'mensaje':'Registro exitoso!','evento':evento,'patrocinador':patrocinador}

    else:
        ctx={'mensaje':'Error en los datos.','evento':evento,'patrocinador':patrocinador}

    return render(request,'Evento/alta_eve_patro.html',ctx)

@login_required(login_url='/')
def Con_Eve_Patro(request):
    obj = Eve_Patro.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Evento/con_eve_patro.html',ctx)

@login_required(login_url='/')
def Alta_Patrocinador(request):
    # form = Form_Patrocinador()
    ctx={'mensaje': 'Ingrese datos de nuevo patrocinador'}

    if request.POST:
        t= Patrocinador()

        t.nombre = request.POST.get('nombre')
        t.ape_pat = request.POST.get('ape_pat')
        t.ape_mat = request.POST.get('ape_mat')
        t.rfc = request.POST.get('rfc')
        t.tel = request.POST.get('tel')
        t.email = request.POST.get('email')

        t.save()
        # form = Form_Patrocinador()

        ctx={'mensaje':'Registro exitoso!'}

    else:
        ctx={'mensaje':'Error en los datos.'}

    return render(request,'Evento/alta_patro.html',ctx)

@login_required(login_url='/')
def Con_Patrocinador(request):
    obj = Patrocinador.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Evento/con_patro.html',ctx)

@login_required(login_url='/')
def Alta_Evento(request):
    # form = Form_Evento()
    tevento = Tevento.objects.all()
    estado = Eve_Edo.objects.all()

    ctx={'mensaje': 'Ingrese datos de nuevo evento','tevento':tevento,'estado':estado}

    if request.POST:
        t= Evento()

        teve = Tevento.objects.get(id=request.POST.get('teve'))
        edo = Eve_Edo.objects.get(id=request.POST.get('estado'))

        t.nombre = request.POST.get('nombre')
        t.descr = request.POST.get('descr')
        t.lugar = request.POST.get('lugar')
        t.fecha = request.POST.get('fecha')
        t.id_tevento = teve
        t.id_eve_edo = edo

        t.save()
        # form = Form_Evento()

        ctx={'mensaje':'Registro exitoso!','tevento':tevento,'estado':estado}

    else:
        ctx={'mensaje':'Error en los datos.','tevento':tevento,'estado':estado}

    return render(request,'Evento/alta_eve.html',ctx)

@login_required(login_url='/')
def Con_Evento(request):
    obj = Evento.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Evento/con_eve.html',ctx)
