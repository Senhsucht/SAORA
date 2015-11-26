from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def Alta_Adoptante(request):
    # form = Form_Adoptante()
    ctx={'mensaje':'Ingrese datos'}

    if request.POST:
        a = Adoptante()

        a.nombre = request.POST.get('nombre')
        a.ape_pat = request.POST.get('ape_pat')
        a.ape_mat = request.POST.get('ape_mat')
        a.edad = request.POST.get('edad')
        a.direccion = request.POST.get('direccion')
        a.tel = request.POST.get('telefono')
        a.email = request.POST.get('email')

        a.save()

        # form = Form_Adoptante()
        ctx={'mensaje': 'Adoptante guardado con exito!'}

    else:

        ctx={'mensaje': 'Error en los datos.'}

    return render(request,'Adopcion/alta_adoptante.html',ctx)

@login_required(login_url='/')
def Con_Adoptante(request):
    obj = Adoptante.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Adopcion/con_adoptante.html',ctx)

@login_required(login_url='/')
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

@login_required(login_url='/')
def Con_Ado_Edo(request):
    obj = Ado_Edo.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Adopcion/con_ado_edo.html',ctx)

@login_required(login_url='/')
def Alta_Adopcion(request):
    # form = Form_Adopcion()
    adoptantes = Adoptante.objects.all()
    animales = Animal.objects.all()
    estados = Ado_Edo.objects.all()
    ctx={'mensaje':'Ingrese datos','adoptantes':adoptantes,'animales':animales,'estados':estados}

    if request.POST:

        adop = request.POST.get('adoptante')
        adop = Afiliado.objects.get(id=adop)

        ani = request.POST.get('animal')
        ani = Animal.objects.get(id=ani)

        edo = request.POST.get('estado')
        edo = Ado_Edo.objects.get(id=edo)

        a = Adopcion()

        a.folio = request.POST.get('folio')
        a.id_adoptante = adop
        a.id_animal = ani
        a.id_ado_edo = edo

        a.save()

        # form = Form_Adopcion()
        ctx={'mensaje': 'Adopcion guardado con exito!','adoptantes':adoptantes,'animales':animales,'estados':estados}

    else:
        ctx={'mensaje': 'Error en los datos.','adoptantes':adoptantes,'animales':animales,'estados':estados}

    return render(request,'Adopcion/alta_adopcion.html',ctx)

@login_required(login_url='/')
def Con_Adopcion(request):
    obj = Adopcion.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Adopcion/con_adopcion.html',ctx)

@login_required(login_url='/')
def Alta_Visita(request):
    adopciones = Adopcion.objects.all()

    # form = Form_Visita()
    ctx={'mensaje':'Ingrese datos','adopciones':adopciones}

    if request.POST:
        adop = request.POST.get('adopciones')
        adop = Adopcion.objects.get(id=adop)

        a = Adopcion()

        a.id_adopcion = adop
        a.no_visita = request.POST.get('visita')
        a.descr = request.POST.get('descr')

        a.save()

        # form = Form_Visita()
        ctx={'mensaje': 'Visita guardado con exito!','adopciones':adopciones}

    else:
        ctx={'mensaje': 'Error en los datos.','adopciones':adopciones}

    return render(request,'Adopcion/alta_visita.html',ctx)

@login_required(login_url='/')
def Con_Visita(request):
    obj = Visita.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Adopcion/con_visita.html',ctx)
