from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def register(request):
    print('inside register')
    if request.method == 'POST':
        print('request.POST')
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user = User.objects.filter(username=username)
        if user:
            return HttpResponse('User already exists')
        if password != confirm_password:
            return HttpResponse('Passwords do not match')
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return HttpResponse('User created')
    return HttpResponse('User not created')

def login(request):
    print('inside login')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username, password)
        login(request, user)
        return HttpResponse('login success')
    
    return HttpResponse('Something went wrong')
