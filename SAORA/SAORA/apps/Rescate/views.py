from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/')
def Alta_Animal(request):
    form = Form_Animal()
    ctx={'mensaje': 'Ingrese datos:','form':form}

    if request.method == 'POST':
        form = Form_Animal(request.POST,request.FILES)

        if form.is_valid():
            a = Animal()

            a.nombre =  form.cleaned_data['Nombre']
            a.id_raza = form.cleaned_data['Raza']
            a.edad = form.cleaned_data['Edad']
            a.imagen = form.cleaned_data['Imagen']

            a.save()

            form = Form_Animal()
            ctx={'mensaje': 'Animal guardado con exito!','form':form}
        else:

            ctx={'mensaje': 'Error en los datos.','form':form}

    return render(request,'Rescate/alta_animal.html',ctx)

@login_required(login_url='/')
def Con_Animal(request):
	obj = Animal.objects.all()
	ctx = {'mensaje':obj}

	return render(request,'Rescate/con_animal.html',ctx)

@login_required(login_url='/')
def Alta_tanimal(request):
        # form = Form_Tanimal()
        ctx={'mensaje': 'Ingrese datos:'}

        if request.POST:
            a = Tanimal()

            a.tanimal =  request.POST.get('tani')
            a.descr = request.POST.get('descr')

            a.save()

            # form = Form_Tanimal()
            ctx={'mensaje': 'Tipo de animal guardado con exito!'}
        else:
            ctx={'mensaje': 'Error en los datos.'}

        return render(request,'Rescate/alta_tanimal.html',ctx)

@login_required(login_url='/')
def Con_tanimal(request):
	obj = Tanimal.objects.all()
	ctx = {'mensaje':obj}

	return render(request,'Rescate/con_tanimal.html',ctx)

@login_required(login_url='/')
def Alta_Raza(request):
        # form = Form_Raza()
        tanimal = Tanimal.objects.all()
        ctx={'mensaje': 'Ingrese datos:','tanimal':tanimal}

        if request.POST:
            a = Raza()

            tani = Tanimal.objects.get(id=request.POST.get('tanimal'))

            a.raza = request.POST.get('raza')
            a.id_tanimal =  tani
            a.descr = request.POST.get('descr')

            a.save()

            # form = Form_Raza()
            ctx={'mensaje': 'Raza guardado con exito!','tanimal':tanimal}

        else:
            ctx={'mensaje': 'Error en los datos.','tanimal':tanimal}

        return render(request,'Rescate/alta_raza.html',ctx)

@login_required(login_url='/')
def Con_Raza(request):
	obj = Raza.objects.all()
	ctx = {'mensaje':obj}

	return render(request,'Rescate/con_raza.html',ctx)

@login_required(login_url='/')
def Alta_Rescate(request):
        form = Form_Rescate()
        ctx={'mensaje': 'Ingrese datos:','form':form}

        if request.method == 'POST':
            form = Form_Rescate(request.POST,request.FILES)

            if form.is_valid():
                a = Rescate()

                a.folio = forms.cleaned_data['Folio']
                a.id_raza = forms.cleaned_data['Afiliado']
                a.id_animal =  form.cleaned_data['Animal']
                a.lugar = form.cleaned_data['Lugar']

                a.save()

                form = Form_Rescate()
                ctx={'mensaje': 'Rescate guardado con exito!','form':form}

            else:
                ctx={'mensaje': 'Error en los datos.','form':form}

        return render(request,'Rescate/alta_rescate.html',ctx)

@login_required(login_url='/')
def Con_Rescate(request):
	obj = Rescate.objects.all()
	ctx = {'mensaje':obj}

	return render(request,'Rescate/con_rescate.html',ctx)
