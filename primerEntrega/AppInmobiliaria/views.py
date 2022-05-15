from multiprocessing import context
from django.shortcuts import render
from .models import Contactos, Departamentos, Casas

# Create your views here.

def inicio(request):

    return render(request, "AppInmobiliaria/inicio.html")

def casas(request):
    if request.method == 'POST':
        direccion = request.POST['direccion']
        numero = request.POST['numero']
        pisos = request.POST['pisos']
        habitaciones = request.POST['habitaciones']
        banos = request.POST['banos']
        precio = request.POST['precio']
        casas = Casas(direccion=direccion, numero=numero, pisos=pisos, habitaciones=habitaciones, banos=banos, precio=precio)
        casas.save()
        return render(request, 'AppInmobiliaria/inicio.html')

    casa = Casas.objects.all()
    context = {'casa':casa}
    return render(request, 'AppInmobiliaria/casas.html', context)

def departamentos(request):
    
    if request.method == 'POST':
        direccion = request.POST['direccion']
        numero = request.POST['numero']
        pisos = request.POST['pisos']
        habitaciones = request.POST['habitaciones']
        banos = request.POST['banos']
        precio = request.POST['precio']
        expensas = request.POST['expensas']
        departamentos = Departamentos(direccion=direccion, numero=numero, pisos=pisos, habitaciones=habitaciones, banos=banos, precio=precio, expensas=expensas)
        departamentos.save()
        return render(request, 'AppInmobiliaria/inicio.html')

    depto = Departamentos.objects.all()
    context = {'depto':depto}
    return render(request, 'AppInmobiliaria/departamentos.html', context)


def contactos(request):


    if request.method == 'POST':
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            telefono = request.POST['telefono']
            mail = request.POST['mail']
            contacto = Contactos(nombre=nombre, apellido=apellido, telefono=telefono, mail=mail)
            contacto.save()
            return render(request, 'AppInmobiliaria/inicio.html')

            
    contacto = Contactos.objects.all()
    context = {'contacto':contacto}
    return render(request, 'AppInmobiliaria/contactos.html', context)

def buscaralquiler(request):
    if request.GET['precio']:
        precio = request.GET['precio']
        valor = Departamentos.objects.filter(precio=precio)
        return render(request, "AppInmobiliaria/buscaralquiler.html", {'valor':valor})
    else:
        respuesta = "No se encontro lo buscado"
        return render(request, 'AppInmobiliaria/inicio.html',{'respuesta':respuesta}) 

    return render(request, 'AppInmobiliaria/buscaralquiler.html')

def buscarcasa(request):
    if request.GET['precio']:
        precio = request.GET['precio']
        valor = Casas.objects.filter(precio=precio)
        return render(request, "AppInmobiliaria/buscarcasa.html", {'valor':valor})
    else:
        respuesta = "No se encontro lo buscado"
        return render(request, 'AppInmobiliaria/inicio.html',{'respuesta':respuesta})
    return render(request, 'AppInmobiliaria/buscarcasa.html')
