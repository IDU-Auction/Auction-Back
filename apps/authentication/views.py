from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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

    return render(request, 'login.html')


def sign_up(request):

    if request.POST:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        existing_username = User.objects.filter(username=username).first()
        if not existing_username:
            existing_email = User.objects.filter(email=email).first()
            if not existing_email:
                user = User(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                )
                user.set_password(password)
                user.save()
                return redirect('login')
            else:
                return redirect('register')
        else:
            return redirect('register')

    return render(request, 'register.html')


def sign_out(request):
    logout(request)
    return redirect('main')
