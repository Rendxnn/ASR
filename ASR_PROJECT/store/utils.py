import csv
from PIL import Image

from .models import Ladrillo



def crear_ladrillos():
    with open('store/Inventario_diario_noviembre_2023_al_15.csv', 'r') as inventario:
        lector = csv.reader(inventario)
        for _ in range(46):
            next(lector)
        for linea in lector:
            nombre = linea[11]
            descripcion = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut suscipit magna nec sem commodo, ullamcorper consequat leo mollis."
            imagen = None
            precio = 9999
            nuevo = Ladrillo(nombre=nombre, descripcion=descripcion, imagen=imagen, precio=precio)
            nuevo.save()
        inventario.close()


def leer_inventario():
    existencias = {}
    with open('store/Inventario_diario_noviembre_2023_al_15.csv', 'r') as inventario:
        lector = csv.reader(inventario)
        for _ in range(46):
            next(lector)
        for linea in lector:
            referencia = linea[11]
            cantidad = linea[12]
            existencias[referencia] = int(cantidad.replace(',', ''))
        inventario.close()
    return existencias


