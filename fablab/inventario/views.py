from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required


from .form import articleform, consumiblesform, solicitudform, categoriaform
from usuarios.forms import regis


# Crear categoria
@permission_required(login_url='/', perm='crearcate')
@login_required(login_url='/')
def crearcate(request):
    if request.method == 'POST':
        maq_form = categoriaform(request.POST)
        if maq_form.is_valid():
            maq_form.save()
            return redirect('maquinas')
    else:
        maq_form= categoriaform()
    return render(request,"admtemp/cat.html",{'maq_form':maq_form})


# superuser
@permission_required(login_url='/', perm='solic')
@login_required(login_url='/')
def solic(request):
    nueva=solicitud.objects.all()
    paginator = Paginator(nueva,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"solicitudes.html",{'nueva':page_obj})

@permission_required(login_url='/', perm='Usuarios')
@login_required(login_url='/')
def Usuarios(request):
    nueva=User.objects.all()
    paginator = Paginator(nueva,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"admtemp/admuser.html",{'nueva':page_obj})


# editar usuario


@permission_required(login_url='/', perm='edituser')
@login_required(login_url='/')
def edituser(request,id):
    consu= User.objects.get(id = id)
    if request.method == 'GET':
        us_form = regis(instance= consu)
    else:
        us_form = regis(request.POST, instance= consu)
        if us_form.is_valid():
            us_form.save()
        redirect('admuser')
    return render(request,'authenticate/registrar_usuario.html',{'form':us_form})


# busqueda usuario

@permission_required(login_url='/', perm='busquedausuario')
@login_required(login_url='/')
def busquedausuario(request):
    if request.method == "POST":
        buscado = request.POST['buscado']
        usuario = User.objects.filter(first_name__contains=buscado)
        return render(request, 'fu/busquedausuario.html', {'buscado':buscado, 'usuario':usuario})
    else:
        return render(request, 'fu/busquedausuario.html', {})



# borrar usuario

@permission_required(login_url='/', perm='borrus')
@login_required(login_url='/')
def borrus(request,n):
    bo= User.objects.get(pk = n)
    bo.delete()
    return redirect('admuser')



# Usuario regular
@login_required(login_url='/')
def maquinas(request):
    nueva=maquina.objects.all()
    paginator = Paginator(nueva,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"maquinas.html",{'nueva':page_obj})


@login_required(login_url='/')
def Consumibles(request):
    nuevo=consumibles.objects.all()
    paginator = Paginator(nuevo,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"consumibles.html",{'nuevo':page_obj})


@login_required(login_url='/')
def uso(request):
    nueva=maquina.objects.all()
    paginator = Paginator(nueva,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"uso.html",{'nueva':page_obj})


@login_required(login_url='/')
def mantenimiento(request):
    nueva=maquina.objects.all()
    paginator = Paginator(nueva,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"mantenimiento.html",{'nueva':page_obj})

    # CRUD MAQUINAS

# crear maquina

@login_required(login_url='/')
def crearmaq(request):
    if request.method == 'POST':
        maq_form = articleform(request.POST)
        if maq_form.is_valid():
            maq_form.save()
            return redirect('maquinas')
    else:
        maq_form= articleform()
    return render(request,"fu/categoria.html",{'maq_form':maq_form})


# busqueda maquina

@login_required(login_url='/')
def busquedamaq(request):
    if request.method == "POST":
        buscado = request.POST['buscado']
        maqui = maquina.objects.filter(nombre__contains=buscado)
        return render(request, 'fu/busqueda.html', {'buscado':buscado, 'producto':maqui})
    else:
        return render(request, 'fu/busqueda.html', {})

# editar maquina

@login_required(login_url='/')
def edit(request,id):
    maqui= maquina.objects.get(id = id)
    if request.method == 'GET':
        maq_form = articleform(instance= maqui)
    else:
        maq_form = articleform(request.POST, instance= maqui)
        if maq_form.is_valid():
            maq_form.save()
        redirect('maquinas')
    return render(request,"fu/categoria.html",{'maq_form':maq_form})

# eliminar maquina

@login_required(login_url='/')
def borr(request,n):
    bo= maquina.objects.get(pk = n)
    bo.delete()
    return redirect('maquinas')



# CRUD CONSUMIBLES

# crear consumible
@login_required(login_url='/')
def crearconsu(request):
    if request.method == 'POST':
        consu_form = consumiblesform(request.POST)
        if consu_form.is_valid():
            consu_form.save()
            return redirect('Consumibles')
    else:
        consu_form= consumiblesform()
    return render(request,"fu/consu.html",{'consu_form':consu_form})


# busqueda consumible
@login_required(login_url='/')
def busquedaconsumible(request):
    if request.method == "POST":
        buscado = request.POST['buscado']
        consumible = consumibles.objects.filter(nombre__contains=buscado)
        return render(request, 'fu/busquedaconsu.html', {'buscado':buscado, 'consumible':consumible})
    else:
        return render(request, 'fu/busquedaconsu.html', {})



# editar consumible
@login_required(login_url='/')
def editconsu(request,id):
    consu= consumibles.objects.get(id = id)
    if request.method == 'GET':
        consu_form = consumiblesform(instance= consu)
    else:
        consu_form = consumiblesform(request.POST, instance= consu)
        if consu_form.is_valid():
            consu_form.save()
        redirect('Consumibles')
    return render(request,"fu/consu.html",{'consu_form':consu_form})

# borrar consumible
@login_required(login_url='/')
def borrconsu(request,n):
    bo= consumibles.objects.get(pk = n)
    bo.delete()
    return redirect('Consumibles')


# CRUD solicitud

# crear solicitud
@login_required(login_url='/')
def enviar(request):
    if request.method == 'POST':
        soli_form = solicitudform(request.POST)
        if soli_form.is_valid():
            soli_form.save()
            return redirect('enviar')
    else:
        soli_form= solicitudform()
    return render(request,"envsolicitud.html",{'maq_form':soli_form})

# editar solicitud
@login_required(login_url='/')
def editarso(request,id):
    soli= solicitud.objects.get(id = id)
    if request.method == 'GET':
        soli_form = solicitudform(instance= soli)
    else:
        soli_form = solicitudform(request.POST, instance= soli)
        if soli_form.is_valid():
            soli_form.save()
        redirect('solicitud')
    return render(request,"envsolicitud.html",{'maq_form':soli_form})

# eliminar solicitud
@permission_required(login_url='/', perm='borrarso')
@login_required(login_url='/')
def borrarso(request,n):
    bor= solicitud.objects.get(pk = n)
    bor.delete()
    return redirect('solic')