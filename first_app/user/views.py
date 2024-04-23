from django.shortcuts import render

# Create your views here.

def login(requests):
    return render(requests, 'user/login.html')

def reg(requests):
    return render(requests, 'user/reg.html')