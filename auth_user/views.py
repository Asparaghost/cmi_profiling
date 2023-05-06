from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from consortium.models import CMI
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def nav(request):
    return render(request, "consortium/nav.html")

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/signup')
    else:
        form = SignUpForm()
    return render(request,'registration/signup.html', {'form':form})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.researcher:
                login(request, user)
                return redirect('/')
            elif user is not None and user.secretariat:
                login(request, user)
                return redirect('/')
            elif user is not None and user.stakeholder:
                login(request, user)
                return redirect('/')
            elif user is not None and user.is_superuser:
                login(request, user)
                return redirect('/')
            else:
                msg = 'Wrong username or password'
        else:
            msg = 'error validating form'
    return render(request, 'registration/login.html', {'form': form, 'msg': msg})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')
