from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Customer
from django.contrib import messages

def signout(request):
    logout(request)
    return redirect('home')

# Create your views here.

def account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            print(request.POST)
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')

            #create user accounts

            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )

            # create customer account
            customer=Customer.objects.create(
                user=user,
                phone=phone,
                address=address
            )

            success_message="Registered Successfully"
            messages.success(request,success_message)

        except Exception as e:
            print(e)
            error_message="User already exist!"
            messages.error(request,error_message)

    if request.POST and 'login' in request.POST:
        context['register']=False
        print(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        user=authenticate(username=username,password=password)
        print(user)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid user')

    return render(request,'account.html',context)