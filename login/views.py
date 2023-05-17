from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    
    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request, 'home.html', {})