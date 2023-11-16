from django.shortcuts import render
from . import utils
from .models import Ladrillo

def home(request):
    ladrillos = Ladrillo.objects.all()
    generar = request.GET.get('generar')
    existencias = utils.leer_inventario()
    print(existencias)
    return render(request, 'store/home.html', {'ladrillos': ladrillos, 'existencias': existencias})
