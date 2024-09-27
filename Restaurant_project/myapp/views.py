from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirmPassword = request.POST.get('password2')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')  # Redirect to home page or dashboard
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please login.')
        if password != confirmPassword:
            messages.error(request, 'Passwords do not match.')
        
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            return redirect('home')  # Redirect to home if login is successful
        else:
            # Handle invalid credentials
            if not User.objects.filter(username=username).exists():
                messages.error(request, 'The username does not exist.')
            else:
                messages.error(request, 'The password is incorrect.')
    
    return render(request, 'registration/login.html')