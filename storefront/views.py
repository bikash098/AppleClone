from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {"products":products})

def signupuser(request):
    form = UserCreationForm()
    if request.method == "GET":
        return render(request,'signup.html', {'form':form})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {'error':'Enter an unique username'})
        else:
            return render(request,'signup.html',{'form':form, 'error':'Password didnt match'})


def loginuser(request):
    form = AuthenticationForm()
    if request.method =='GET':
        return render(request, 'login.html', {'form':form})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'form':form, "error":'No such user found'})
        else:
            login(request, user)
            return redirect('home')
            
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')







    