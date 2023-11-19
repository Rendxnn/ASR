from django.shortcuts import render, get_object_or_404, redirect
from . import utils
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ladrillo as Product, Ladrillo
from cart.models import Cart


def home(request):
    ladrillos = Ladrillo.objects.all()
    if len(ladrillos) == 0:
        utils.crear_ladrillos()
    existencias = utils.leer_inventario()
    if 'generar_pedido' in request.POST:
        for ladrillo in ladrillos:
            cantidad_ladrillo = int(request.POST[f'{ladrillo.id}_cantidad'])
            if cantidad_ladrillo > 0:
                nuevo_cart = Cart(product=ladrillo, quantity=cantidad_ladrillo)
                nuevo_cart.save()
        return redirect('cart/home_cart')
    return render(request, 'store/home.html', {'ladrillos': ladrillos, 'existencias': existencias})


""" 
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        messages.success(request, f"{product.name} added to your cart.")
        return redirect("cart:add_to_cart", product_id=product.id)

    context = {
        "product": product,
    }

    return render(request, "store/home.html", context)
"""
