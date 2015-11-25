from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User , Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

# Create your views here.

def index(request):
	ctx = { 'mensaje': "BIENVENIDOS"}

	if request.POST:
		usu = request.POST.get('Usr')
		contra = request.POST.get('Pwd')
		u = Usuario()
		try:
			u = Usuario.objects.get(usr=usu,pwd=contra,activo=True)
		except Usuario.DoesNotExist:
			u.usr = 'noope'

		if usu == u.usr :
			ctx = { 'mensaje': "Encontrado"}
			return redirect('/usr/alta_afil/')
			# return render(request,'General/system.html',ctx)
		else:
			ctx = { 'mensaje': 'Error al inicio de sesion'}

	return render(request,'General/index.html',ctx)

@login_required(login_url='/')
def Alta_Afil(request):
	form = Form_Afil()
	ctx={'mensaje': 'Ingrese datos:','form':form}

	if request.method == "POST":
		form =  Form_Afil(request.POST, request.FILES)

		if form.is_valid():
			a = Afiliado()

			a.nombre = form.cleaned_data['Nombre']
			a.ape_pat = form.cleaned_data['Apellido_Paterno']
			a.ape_mat = form.cleaned_data['Apellido_Materno']
			a.edad = form.cleaned_data['Edad']
			a.direccion = form.cleaned_data['Direccion']
			a.tel = form.cleaned_data['Telefono']
			a.email = form.cleaned_data['Email']
			a.id_tafil = form.cleaned_data['Tipo_de_Afiliado']
			a.imagen = form.cleaned_data['Imagen']

			a.save()

			form = Form_Afil()
			ctx={'mensaje': 'Afiliado guardado con exito!','form':form}

		else:
			form = Form_Afil()
			ctx={'mensaje': 'Error en los datos.','form':form}

	return render(request,'Usuarios/alta_afil.html',ctx)

@login_required(login_url='/')
def Alta_Usr(request):
	# form = Form_Usr()
	afiliados = Afiliado.objects.all()
	tusuario = Tusr.objects.all()
	ctx={'mensaje': 'Ingrese datos:'}

	if request.method == "POST":
		form =  Form_Usr(request.POST, request.FILES)

		if form.is_valid():
			u = Usuario()


			u.usr = form.cleaned_data['Usuario']
			u.pwd = form.cleaned_data['Contrasena']
			u.id_afil = form.cleaned_data['Afiliado']
			u.id_tusr = form.cleaned_data['Tipo_de_Usuario']

			u.save()

			form = Form_Usr()
			ctx={'mensaje': 'Usuario registrado correctamente!'}

		else:
			form = Form_Usr()
			ctx={'mensaje': 'Error en los datos.'}

	return render(request,'Usuarios/alta_usr.html',ctx)

@login_required(login_url='/')
def Con_Afil(request):
	# form = Select_Tafil()
	obj = Afiliado.objects.all()
	ctx = {'mensaje':obj}

	# if request.method == "POST":
	# 	form = Select_Tafil(request.POST)

	# 	if form.is_valid():

	# 		nom = request.POST.get('nombre')
	# 		ap= request.POST.get('ape_pat')
	# 		am = request.POST.get('ape_mat')
	# 		tafil = form.cleaned_data['Tafil']

	return render(request,'Usuarios/con_afil.html',ctx)

@login_required(login_url='/')
def Con_Usr(request):
	# form = Select_Tusr()
	obj = Usuario.objects.all()
	ctx = {'mensaje':obj}

	return render(request,'Usuarios/con_usr.html',ctx)

@login_required(login_url='/')
def Alta_tusr(request):
    form = Form_Tusr()
    ctx={'mensaje': 'Ingrese datos de nuevo tipo de usuario','form':form}

    if request.method == 'POST':
        form = Form_Tusr(request.POST,request.FILES)

        if form.is_valid():
            t= Tusr()

            t.tusr = form.cleaned_data['Tipo_de_Usuario']
            t.descr = form.cleaned_data['Descripcion']

            t.save()
            form = Form_Tusr()

            ctx={'mensaje':'Registro exitoso!','form':form}
        else:
            ctx={'mensaje':'Error en los datos.','form':form}

    return render(request,'Usuarios/alta_tusr.html',ctx)

@login_required(login_url='/')
def Con_tusr(request):
    obj = Tusr.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Usuarios/con_tusr.html',ctx)

@login_required(login_url='/')
def Alta_tafil(request):
    form = Form_Tafil()
    ctx={'mensaje': 'Ingrese datos de nuevo tipo de usuario','form':form}

    if request.method == 'POST':
        form = Form_Tafil(request.POST,request.FILES)

        if form.is_valid():
            t= Tafil()

            t.tusr = form.cleaned_data['Tipo_de_Afiliado']
            t.descr = form.cleaned_data['Descripcion']

            t.save()
            form = Form_Tafil()

            ctx={'mensaje':'Registro exitoso!','form':form}
        else:
            ctx={'mensaje':'Error en los datos.','form':form}

    return render(request,'Usuarios/alta_tafil.html',ctx)

@login_required(login_url='/')
def Con_tafil(request):
    obj = Tafil.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Usuarios/con_tafil.html',ctx)
