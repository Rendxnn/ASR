from django.shortcuts import render

def home_cart(request):
    return render(request, 'cart/home_cart.html', {})

