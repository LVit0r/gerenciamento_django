from django.shortcuts import render,redirect
from django.contrib.auth import logout 

def logout(request):
    auth.logout(request)
    return redirect('login')
