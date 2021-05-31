from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from store.models import Order
from store.models.customer import Customer
from store.middlewares.auth import auth_middleware


class Orders(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        customer_id=request.session['customer']
        orders=Order.get_orders_by_customer(Customer.get_customer_by_id(customer_id))
        return render(request,'orders.html',{'orders':orders})

