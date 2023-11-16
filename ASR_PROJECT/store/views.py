from django.shortcuts import render
from . import utils

def home(request):
    generar = request.GET.get('generar')
    return render(request, 'store/home.html', {})
