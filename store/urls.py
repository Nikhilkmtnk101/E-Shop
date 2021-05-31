from django.contrib import admin
from django.urls import path
from store.views import index, login, sign_up, cart, check_out, orders

urlpatterns = [
    path('',index.Index.as_view(),name='home_page'),
    path('signup',sign_up.SignUp.as_view(),name='sign_up_page'),
    path('login',login.Login.as_view(),name='login'),
    path('logout',login.logout,name='logout'),
    path('cart',cart.Cart.as_view(),name='cart_page'),
    path('check_out',check_out.CheckOut.as_view(),name='check_out'),
    path('orders',orders.Orders.as_view(),name='orders_page')
]