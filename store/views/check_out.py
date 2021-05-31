from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views import View

from store.middlewares.auth import auth_middleware
from store.models import Product, Order
from store.models.customer import Customer


class CheckOut(View):
    @method_decorator(auth_middleware)
    def post(self,request):
        phone_number=request.POST.get('phone_number')
        address=request.POST.get('address')
        customer_id=request.session.get('customer')
        customer=Customer.get_customer_by_id(customer_id)
        cart=request.session.get('cart')
        products=Product.get_products_by(list(cart.keys()))
        if not products:
            request.session['cart'] = {}
            return redirect('cart_page')
        for product in products:
            quantity = cart.get(str(product.id))
            order=Order(product=product,customer=customer,address=address,
                        phone_number=phone_number,quantity=quantity,total_price=quantity*product.price)
            order.place_order()
        request.session['cart']={}
        return redirect('cart_page')
