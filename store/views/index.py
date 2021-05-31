from django.shortcuts import render,redirect
from django.views import View
from store.models.products import Product
from store.models.category import Category


class Index(View):

    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1;
                else:
                    cart[product] = quantity + 1;
            else:
                cart[product]=1;
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        print(cart)
        return redirect('home_page')

    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        product = None
        categories = Category.get_all_categories()
        category = request.GET.get('category')
        if category:
            product = Product.get_all_products_specific_category(category)
        else:
            product = Product.get_all_products()
        data = {}
        data['products'] = product
        data['categories'] = categories
        return render(request, 'index.html', data)

