from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from valinix import validate_password, ValidationError

def signup_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User already exists")
            else:
                try:
                    validate_password(password=password1)
                    user = User.objects.create_user(username=username, password=password1)
                    user.save()
                    messages.success(request, 'Signup Successfull. Proceed for login..')
                    return redirect('login')
                except ValidationError as error_msg:
                    messages.error(request, error_msg)
        else:
            messages.error(request, "Password does not match")

    context = {
        'title':'SignUp User',
    }
    return render(request, 'signup.html', context)


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            
    context = {
        'title':'LogIn User',
    }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')

