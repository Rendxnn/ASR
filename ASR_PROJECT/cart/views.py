from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart
from store.models import Ladrillo
from . import utils
import os
from django.http import HttpResponse
from django.conf import settings


def home_cart(request):
    if not request.user.is_authenticated:
        return redirect('home')
    cart_items = Cart.objects.all().filter(user=request.user)
    total_price = sum(pedido.product.precio for pedido in cart_items)
    if 'generar_factura' in request.POST:
        utils.generate_receipt(cart_items, total_price, request.user.username)
        file_path = os.path.join(settings.MEDIA_ROOT, f'receipts/receipt{request.user.username.__str__()}.pdf')
        print(file_path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                return response
        else:
            return HttpResponse('El archivo no existe.')
    return render(request, 'cart/home_cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, producto_id):
    cart_item = Cart.objects.filter(pk=producto_id).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item added to your cart.")
    else:
        instance = Ladrillo.objects.get(pk=producto_id)
        Cart.objects.create(product=instance)
        messages.success(request, "Item added to your cart.")

    return redirect("cart_detail")


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, pk=cart_item_id)
    cart_item.delete()
    messages.success(request, "Item removed from your cart.")
    return redirect("cart_detail")


def cart_detail(request):
    cart_items = Cart.objects.all().filter(user=request.user)
    total_price = sum(item.quantity * item.product.precio for item in cart_items)

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(request, "cart/home_cart.html", context)
