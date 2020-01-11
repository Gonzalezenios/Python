# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from.models import Comanda

def index(request):
    return render(request, 'pedidos/index.html')

def guardar_pedidos(request):
    print(request.POST['orden'], request.POST['usuario'], request.POST['ubicacion'])
    comanda = Comanda(orden = request.POST['orden'], usuario = request.POST['usuario'], ubicacion = request.POST['ubicacion'])
    comanda.save()
    return HttpResponse ('Su pedido será entregado pronto')