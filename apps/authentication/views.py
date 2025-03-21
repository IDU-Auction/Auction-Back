from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User

from .models import CustomUser


def sign_in(request):

    if request.POST:
        phone_number = '+998' + request.POST.get('phone_number').replace('-', '').strip()
        password = request.POST.get('password')
        custom_user = CustomUser.objects.filter(phone_number=phone_number).first()
        if custom_user:
            print(custom_user)
            print(custom_user.check_password(password))
            if custom_user.check_password(password):
                print('phone_number:', phone_number)
                print('password:', password)
                # user = authenticate(request, username=phone_number, password=password)
                # print('user:', user)
                # if user:
                login(request, custom_user)
                return redirect('main')
        else:
            return redirect('login')

    return render(request, 'authorization.html')


def sign_up(request):

    if request.POST:
        phone_number = '+998' + "".join(request.POST.get('phone_number').split('-'))
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            raise "Passwords should be the same!!!"
            return redirect('register')
        
        existing_phone_number = CustomUser.objects.filter(phone_number=phone_number).first()
        if not existing_phone_number:
            user = CustomUser.objects.create(phone_number=phone_number)
            user.set_password(password1)
            user.save()
            return redirect('login')
        else:
            return redirect('register')

    return render(request, 'registration.html')


def sign_out(request):
    logout(request)
    return redirect('main')
