from django.shortcuts import render
from .models import Persona, Compra, Producto
# Create your views here.

def Compra_list(request):
    compra = Compra.objects.all()
    return render(request, 'Aplicacion/Compra_list.html', {'Compra':compra})


def Persona_list(request):
    persona = Persona.objects.all()
    return render(request, 'Aplicacion/Persona_list.html', {'Persona':persona})


def Producto_list(request):
    producto = Producto.objects.all()
    return render(request, 'Aplicacion/Producto_list.html', {'Producto':producto})


def index(request):
    return render(request, 'Aplicacion/index.html', {})
