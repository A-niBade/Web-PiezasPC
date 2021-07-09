from django.shortcuts import render, redirect, get_object_or_404
from .models import Placa_madre, Procesador, Tarjeta_video
from .forms import PlacaForm, ProcesadorForm, TarjetaForm
from .filters import ProcesadorFiltro, TarjetaFiltro, PlacaFiltro
from django.contrib import messages 

# Create your views here.

def home(request):
    return render (request, 'AppGestion/home.html')

    Proce

def tarjeta_video(request):
    tarjeta = Tarjeta_video.objects.all()
    data = {
        'tarjeta' : tarjeta
    }
    return render (request, 'AppGestion/tarjetas_video.html', data)

def procesadores(request):
    proce = Procesador.objects.all()
    data = {
        'proce' : proce
    }
    return render(request, 'AppGestion/procesadores.html', data)

def placas_madre(request):
    placas = Placa_madre.objects.all()
    data  = {
        'placas' : placas       
    }
    return render(request, 'AppGestion/placas_madre.html', data)

def ingresar(request):
    return render(request, 'AppGestion/ingresar.html')

def ingresar_placa(request):

    data = {
        'formPlaca' : PlacaForm()
    }

    if request.method == 'POST':
        formulario = PlacaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Ingresado Correctamente") 
        else:
            data["formPlaca"] = formulario

    return render(request, 'AppGestion/ingresos/ingresar_placa.html', data)

def ingresar_tarjeta(request):

    data = {
        'formTarjeta' : TarjetaForm()
    }

    if request.method == 'POST':
        formulario = TarjetaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Ingresado Correctamente")
        else:
            data["formTarjeta"] = formulario

    return render(request, 'AppGestion/ingresos/ingresar_tarjeta.html', data)

def ingresar_procesador(request):

    data = {
        'formProcesador' : ProcesadorForm()
    }

    if request.method == 'POST':
        formulario = ProcesadorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Ingresado Correctamente")
        else:
            data["formProcesador"] = formulario
    return render(request, 'AppGestion/ingresos/ingresar_procesador.html', data)

def busqueda(request):
    return render(request,'AppGestion/busqueda.html')

def lista_placas(request):

    placas = Placa_madre.objects.all()

    Filtroplaca = PlacaFiltro(request.GET,queryset=placas)
    placas = Filtroplaca.qs

    data = {
        'placas' : placas,
        'Filtroplacas' : Filtroplaca
    }
    return render(request, 'AppGestion/listados/lista_placas.html', data)

def lista_procesadores(request):

    procesadores = Procesador.objects.all()

    Filtroproces = ProcesadorFiltro(request.GET, queryset=procesadores)
    procesadores = Filtroproces.qs 

    data = {
        'procesadores' : procesadores,
        'Filtroproces' : Filtroproces
    }
    return render(request,'AppGestion/listados/lista_procesadores.html', data)

def lista_tarjetas(request):

    tarjetas = Tarjeta_video.objects.all()

    Filtrotarjetas = TarjetaFiltro(request.GET,queryset=tarjetas)
    tarjetas = Filtrotarjetas.qs

    data = {
        'tarjetas' : tarjetas,
        'Filtrotarjetas' : Filtrotarjetas
    }
    return render(request,'AppGestion/listados/lista_tarjetas.html', data)

def modificar_proce(request, id):

    procesadores = get_object_or_404(Procesador, id=id)

    data = {
        'formProcesador' : ProcesadorForm(instance=procesadores)
    }

    if request.method == 'POST':
        formulario = ProcesadorForm(data=request.POST, instance=procesadores,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to= "lista_procesadores")
        else:
            data["formProcesador"] = formulario

    return render (request, 'AppGestion/modificados/modificar_proce.html', data)

def modificar_placa(request, id):

    placas = get_object_or_404(Placa_madre, id=id)

    data = {
        'formPlaca' : PlacaForm(instance=placas)
    }

    if request.method == 'POST':
        formulario = PlacaForm(data=request.POST, instance=placas,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to= "lista_placas")
        else:
            data["formPlaca"] = formulario

    return render (request, 'AppGestion/modificados/modificar_placa.html', data)

def modificar_tarjeta(request, id):

    tarjetas = get_object_or_404(Tarjeta_video, id=id)

    data = {
        'formTarjetas' : TarjetaForm(instance=tarjetas)
    }

    if request.method == 'POST':
        formulario = TarjetaForm(data=request.POST, instance=tarjetas,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to= "lista_tarjetas")
        else:
            data["formTarjetas"] = formulario

    return render (request, 'AppGestion/modificados/modificar_tarjeta.html', data)

def eliminar_proce(request, id):
    procesador = get_object_or_404(Procesador, id = id)
    procesador.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to = "lista_procesadores")

def eliminar_placa(request, id):
    placa = get_object_or_404(Placa_madre, id= id)
    placa.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to = "lista_placas")

def eliminar_tarjeta(request, id):
    tarjeta = get_object_or_404(Tarjeta_video, id = id)
    tarjeta.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to = "lista_tarjetas")



