from django.shortcuts import render, get_object_or_404 , redirect
from . import utils
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ladrillo as Product, Ladrillo

def home(request):
    ladrillos = Ladrillo.objects.all()
    generar = request.GET.get('generar')
    existencias = utils.leer_inventario()
    print(existencias)
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