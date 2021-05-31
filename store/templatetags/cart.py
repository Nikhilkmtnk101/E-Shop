from django import template
register=template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    for key in keys:
        if int(key)==product.id:
            return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    quantity=cart.get(str(product.id))
    if quantity:
        return quantity
    else:
        return 0;


@register.filter(name='price_total')
def price_total(product,cart):
    return  product.price*cart_quantity(product,cart)


@register.filter(name='total_cart_price')
def total_cart_price(products,cart):
    sum=0
    if not products:
        return sum
    for product in products:
        sum+=price_total(product,cart)
    return sum


@register.filter(name='length')
def length(cart):
    sum=0
    if not cart:
        return sum
    for val in cart.values():
        sum+=val
    return sum

@register.filter(name='multiply')
def multiply(a,b):
    if not a or not b:
        return 0
    return a*b






