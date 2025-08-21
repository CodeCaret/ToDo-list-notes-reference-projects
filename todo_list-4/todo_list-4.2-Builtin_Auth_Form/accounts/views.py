from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


# Extended UserCreationForm
from accounts.forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup Successfull. Proceed for login..')
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()

    context = {
        'title':'SignUp User',
        'form':form,
    }
    return render(request, 'signup.html', context)


# Simple UserCreationForm
# from django.contrib.auth.forms import UserCreationForm
# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Signup Successfull. Proceed for login..')
#             return redirect('login')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = UserCreationForm()

#     context = {
#         'title':'SignUp User',
#         'form':form,
#     }
#     return render(request, 'signup.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user=user)
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AuthenticationForm()
        
    context = {
        'title':'LogIn User',
        'form':form,
    }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')

