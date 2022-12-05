from django.shortcuts import render, redirect
from .models import equipo_medico, traslado, prestamo, cupo, equipo_en_cupo, matrona, matrona_clinica, matrona_coordinadora
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import nuevoEquipoForm, nuevoPrestamoForm, nuevoTrasladoForm

# Create your views here.

def loginView(request):
    return render(request, 'registration/login.html')


def homeInventario(request):
    equipo =equipo_medico.objects.all()

    busqueda = request.GET.get("buscar")
    por_tipo = request.GET.get("buscar-tipo")

    if busqueda:
        equipo = equipo_medico.objects.filter(Q(id_equipo = busqueda)|Q(tipo_equipo = por_tipo)).distinct()

    return render(request, 'core/baseHome.html', {'equipo':equipo})

def enCupo(request):
    en_cupo = equipo_en_cupo.objects.all()

    busqueda = request.GET.get("buscar")

    if busqueda:
        en_cupo = equipo_en_cupo.objects.filter(id_equipo = busqueda).distinct()

    return render(request, 'core/baseHome.html', {'en_cupo':en_cupo})

def traslados(request):
    traslados = traslado.objects.all()

    busqueda = request.GET.get("buscar")

    if busqueda:
        traslados = traslado.objects.filter(id_equipo = busqueda).distinct()

    return render(request, 'core/baseTraslados.html', {'traslado':traslados})

def prestamos(request):
    prestamos = prestamo.objects.all()

    busqueda = request.GET.get("buscar")

    if busqueda:
        prestamos = prestamo.objects.filter(id_equipo = busqueda).distinct()

    return render(request, 'core/basePrestamos.html', {'prestamo':prestamos})


def registrarEquipo(request):
    form = nuevoEquipoForm(request.POST)
    
    if form.is_valid():
        print('valido')
        form.save()
        return redirect(to='coordinadoraHome')

    else:
        print('invalido')
    
    return render(request, 'core/nuevoEquipo.html', {'form':form})

def registrarTraslado(request):
    form = nuevoTrasladoForm(request.POST)
    
    if form.is_valid():
        print('valido')
        form.save()
        return redirect(to='clinicaHome')
        
    else:
        print('invalido')
    
    return render(request, 'core/nuevoTraslado.html', {'form':form})

def registrarPrestamo(request):
    form = nuevoPrestamoForm(request.POST)
    
    if form.is_valid():
        print('valido')
        form.save()
        return redirect(to='clinicaHome')
        
    else:
        print('invalido')
    
    return render(request, 'core/nuevoPrestamo.html', {'form':form})


def updateEquipo(request, id):
    equipo = equipo_medico.objects.get(id_equipo=id)
    form = nuevoEquipoForm(request.POST, instance=equipo)

    if form.is_valid():
        form.save()

        return redirect(to='clinicaHome')
    else:
        form = nuevoEquipoForm(instance=equipo)

    return render(request, 'core/updateEquipo.html',{'form':form})
