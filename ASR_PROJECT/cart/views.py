from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart

def home_cart(request):
    return render(request, 'cart/home_cart.html', {})


def add_to_cart(request, producto_id):
    cart_item = Cart.objects.filter(pk = producto_id).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item added to your cart.")
    else:
        Cart.objects.create(product=producto_id)
        messages.success(request, "Item added to your cart.")

    return redirect("cart_detail")


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, pk=cart_item_id)
    cart_item.delete()
    messages.success(request, "Item removed from your cart.")
    return redirect("cart_detail")


def cart_detail(request):
    cart_items = Cart.objects.all()
    total_price = sum(item.quantity * 2 for item in cart_items)

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(request, "cart/home_cart.html", context)
