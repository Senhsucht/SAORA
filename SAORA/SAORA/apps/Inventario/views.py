from django.shortcuts import render
from .models import *
from SAORA.apps.Evento.models import *
from SAORA.apps.Adopcion.models import *
from SAORA.apps.Usuarios.models import *

# Create your views here.

def Alta_Inventario(request):
    productos = Producto.objects.all()
    afiliados = Afiliado.objects.all()
    eventos = Evento.objects.all()
    donantes = Donante.objects.all()


    ctx={'mensaje':'Ingrese datos','productos':productos,'eventos':eventos,'afiliados':afiliados,'donantes':donantes}

    if request.POST:

        prod = request.POST.get('producto')

        try:
            esta = Inventario.objects.get(id_producto=prod)
        except Inventario.DoesNotExist:
            esta = "NOPE"
        cant = int(request.POST.get('cantidad'))

        h = Inv_Hist()
        i = Inventario()

        prod = Producto.objects.get(id=prod)
        afil = Afiliado.objects.get(id=request.POST.get('afiliado'))
        eve = Evento.objects.get(id=request.POST.get('evento'))
        don = Donante.objects.get(id=request.POST.get('donante'))

        if esta == "NOPE":
            h = Inv_Hist()
            i = Inventario()


            i.id_producto = prod
            i.cantidad = request.POST.get('cantidad')
            i.descr = request.POST.get('descr')

            h.id_afiliado = afil
            h.id_producto = prod
            h.cantidad = cant
            h.descr = request.POST.get('descr')
            h.id_donante =don
            h.id_evento = eve
            h.alta_baja = True

            h.save()
            i.save()

            ctx={'mensaje':'Registrado con exito!','productos':productos,'eventos':eventos,'afiliados':afiliados,'donantes':donantes}
        else:
            h = Inv_Hist()

            esta.cantidad = esta.cantidad + cant

            h.id_afiliado = afil
            h.id_producto = prod
            h.cantidad = cant
            h.descr = request.POST.get('descr')
            h.id_donante = don
            h.id_evento = eve
            h.alta_baja = True

            h.save()
            esta.save()
    else:

        ctx={'mensaje': 'Error en los datos.','productos':productos,'eventos':eventos,'afiliados':afiliados,'donantes':donantes}

    return render(request,'Inventario/alta_inv.html',ctx)

def Con_Inventario(request):
    obj = Inventario.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Inventario/con_inv.html',ctx)

def Con_Inv_Estado(request):
    obj = Inv_Hist.objects.all()
    ctx = {'mensaje':obj}

    if request.POST:
        estado = request.POST.get('alta_baja')

        if estado == "1":
            obj = Inv_Hist.objects.all().filter(alta_baja=True)
            ctx = {'mensaje':obj}
            # return render(request,'Inventario/con_inv_edo.html',ctx)
        else:
            obj = Inv_Hist.objects.all().filter(alta_baja=False)
            ctx = {'mensaje':obj}
            # return render(request,'Inventario/con_inv_edocon_inv_edo.html',ctx)

    return render(request,'Inventario/con_inv_edo.html',ctx)

def Baja_Inventario(request):
        productos = Producto.objects.all()
        afiliados = Afiliado.objects.all()
        eventos = Evento.objects.all()
        donantes = Donante.objects.all()

        ctx={'mensaje':'Ingrese datos de la salida de productos','productos':productos,'eventos':eventos,'afiliados':afiliados,'donantes':donantes}

        if request.POST:

            inv = Inventario.objects.get(id_producto=request.POST.get('producto'))
            prod = Producto.objects.get(id=request.POST.get('producto'))
            cant = int(request.POST.get('cantidad'))
            afil = Afiliado.objects.get(id=request.POST.get('afiliado'))

            if cant <= inv.cantidad:
                h = Inv_Hist()
                inv.cantidad = inv.cantidad - cant

                h.id_afiliado = afil
                h.id_producto = prod
                h.cantidad = cant
                h.descr = request.POST.get('descr')
                h.alta_baja = False

                h.save()
                inv.save()

            else:
                ctx={'mensaje': 'Error: El inventario no dispone con esa cantidad de producto.','productos':productos,'eventos':eventos,'afiliados':afiliados,'donantes':donantes}

        else:

            ctx={'mensaje': 'Error en los datos.','productos':productos,'eventos':eventos,'afiliados':afiliados,'donantes':donantes}

        return render(request,'Inventario/baja_inv.html',ctx)

def Alta_Producto(request):
    ctx={'mensaje':'Ingrese datos del producto'}

    if request.POST:
        p = Producto()

        p.nombre = request.POST.get('nombre')
        p.marca = request.POST.get('marca')
        p.cneto = request.POST.get('cneto')

        p.save()

    else:
        ctx={'mensaje':'Error en los datos'}

    return render(request,'Inventario/alta_prod.html',ctx)

def Con_Producto(request):
    obj = Producto.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Inventario/con_prod.html',ctx)

def Alta_Donante(request):
    ctx={'mensaje':'Ingrese datos del donante'}

    if request.POST:
        p = Donante()

        p.nombre = request.POST.get('nombre')
        p.ape_pat = request.POST.get('ape_pat')
        p.ape_mat = request.POST.get('ape_mat')
        p.rfc = request.POST.get('rfc')
        p.tel = request.POST.get('tel')
        p.direccion = request.POST.get('direccion')
        p.email = request.POST.get('email')

        p.save()

    else:
        ctx={'mensaje':'Error en los datos'}

    return render(request,'Inventario/alta_donante.html',ctx)

def Con_Donante(request):
    obj = Donante.objects.all()
    ctx = {'mensaje':obj}

    return render(request,'Inventario/con_donante.html',ctx)
