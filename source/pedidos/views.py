# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from.models import Comanda

def index(request):
    return render(request, 'pedidos/index.html')

def guardar_pedidos(request):
    print(request.POST['orden'])
    comanda = Comanda(orden = request.POST['orden'])
    comanda.save()
    return HttpResponse ('Su pedido será entregado pronto')
    