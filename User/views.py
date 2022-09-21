from Home.views import *
from django.contrib.auth.models import User
from .models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(username, email, password, password2)
        if password == password2:
            if User.objects.filter(username=username).exists():
                request.session['error'] = 'Username already exists'
                return redirect(error)
            elif User.objects.filter(email=email).exists():
                request.session['error'] = 'Email already exists'
                return redirect(error)
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                userprofile = UserProfile(user=user)
                userprofile.save()
                return redirect(signin)
    else:
        return render(request, 'user/signup.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            request.session['error'] = 'Invalid credentials'
            return redirect(error)
    else:
        return render(request, 'user/signin.html')

def error(request):
    error = request.session['error']
    return render(request, 'user/error.html', {'error': error})



def signout(request):
    logout(request)
    return redirect(signin)


def profile(request, username):
    print(username)
    user = User.objects.get(username=username)
    userprofile = UserProfile.objects.get(user=user)
    return render(request, 'user/profile.html', {'user': userprofile})


