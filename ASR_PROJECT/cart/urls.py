"""PP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cart import views as cartViews
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('home_cart', cartViews.home_cart, name='home_cart'),
    path("add_to_cart/<int:producto_id>/", cartViews.add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<int:cart_item_id>/", cartViews.remove_from_cart, name="remove_from_cart"),
    path("cart_detail", cartViews.cart_detail, name="cart_detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)