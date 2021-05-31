from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views import View

from store.middlewares.auth import auth_middleware
from store.models.products import Product
from store.models.category import Category


class Cart(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        products = None
        if ids:
            products = Product.get_products_by(ids)
        data = {}
        data['products'] = products
        return render(request, 'cart.html', data)
