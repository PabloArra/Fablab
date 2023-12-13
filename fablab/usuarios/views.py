from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import *
from .forms import regis
from django.contrib.auth.decorators import login_required, permission_required




def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('maquinas')
        else:
            messages.success(request, ("Ingrese datos validos"))
            return redirect('/')
    
    else:
        return render(request, 'authenticate/login.html')

@permission_required(login_url='/', perm='registrar_user')
@login_required(login_url='/')
def registrar_user(request):
        if request.method == 'POST':
             form = regis(request.POST)
             if form.is_valid():
                  form.save()
                  return redirect('admuser')
        else:
            form = regis()

        return render(request, 'authenticate/registrar_usuario.html', {'form':form,})

def logout_user(request):
    logout(request)
    return redirect('/')


