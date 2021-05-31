from django.shortcuts import render,redirect
from django.views import View
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password


class SignUp(View):

    def validate_details(self,customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name is Required Field."
        elif len(customer.first_name.replace(" ", "")) == 0:
            error_message = "First Name is Required Field."
        elif len(customer.first_name) < 3:
            error_message = "First Name must be at least 3 chars long."
        elif len(customer.first_name) > 50:
            error_message = "First Name must contain at max 50 chars."
        elif not customer.last_name:
            error_message = "Last Name is Required Field."
        elif len(customer.last_name.replace(" ", "")) == 0:
            error_message = "Last Name is Required Field."
        elif len(customer.last_name) < 3:
            error_message = "Last Name must be at least 3 chars long."
        elif len(customer.last_name) > 50:
            error_message = "Last Name must contain at max 50 chars."
        elif not customer.phone_number:
            error_message = "Phone Number is Required Field."
        elif len(customer.phone_number.replace(" ", "")) < 10:
            error_message = "Invalid Phone Number"
        elif len(customer.phone_number) != 10:
            error_message = "Phone Number must be 10 chars long."
        elif customer.phone_number[0] == '0':
            error_message = "Invalid Phone Number."
        elif not customer.email:
            error_message = "Email is Required Field."
        elif len(customer.email.replace(" ", "")) == 0:
            error_message = "Email is Required Field."
        elif len(customer.email) < 3:
            error_message = "Email must be at least 3 chars long"
        elif len(customer.password) < 6:
            error_message = "Password must be at least 6 chars long"
        return error_message

    def register_customer(self,request,customer):
        error_message = self.validate_details(customer)
        if error_message:
            data = {}
            data['error'] = error_message
            data['values'] = customer
            return render(request, 'sign_up.html', data)
        else:
            error_message = Customer.check_customer(customer)
            if error_message:
                data = {}
                data['error'] = error_message
                data['values'] = customer
                return render(request, 'sign_up.html', data)
            else:
                customer.password = make_password(customer.password)
                customer.add_new_customer()
                return redirect('home_page')

    def get(self,request):
        return render(request, 'sign_up.html')

    def post(self,request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone_number = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone_number=phone_number,
                            email=email,
                            password=password)
        return self.register_customer(request, customer)
