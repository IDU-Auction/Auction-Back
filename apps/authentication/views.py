from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User

from .models import CustomUser


def sign_in(request):

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('main')
        else:
            return redirect('login')

    return render(request, 'authorization.html')


def sign_up(request):

    if request.POST:
        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            raise "Passwords should be the same!!!"
            return redirect('register')
        
        existing_phone_number = CustomUser.objects.filter(phone_number=phone_number).first()
        if not existing_phone_number:
            user = CustomUser.objects.create(phone_number=phone_number, password=password1)
            return redirect('login')
        else:
            return redirect('register')

    return render(request, 'registration.html')


def sign_out(request):
    logout(request)
    return redirect('main')
