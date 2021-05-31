from django.shortcuts import render,redirect
from django.views import View
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password


class Login(View):

    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.find_customer_by_email(email)
        if customer:
            if check_password(password, customer.password):
                request.session['customer']=customer.id
                return redirect('home_page')
            else:
                error_message = "Password is not Correct"
                data = {}
                data['values'] = customer
                data['error'] = error_message
                return render(request, 'login.html', data)
        else:
            error_message = "Email is not Registered"
            return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear();
    return redirect('login')

