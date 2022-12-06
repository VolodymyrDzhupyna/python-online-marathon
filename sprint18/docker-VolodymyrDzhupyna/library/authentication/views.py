"""
Views for authentication
"""
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterCustomUserModelForm, LoginCustomUserModelForm



def registration(request):
    context = {}
    form = RegisterCustomUserModelForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        login(request, user_obj)
        return redirect('authentication:registration_success')
    context['form'] = form

    return render(request, 'authentication/registration.html', context=context)


@login_required
def registration_success(request):
    """Success registration view"""
    text = 'Congratulations! You have successfully registered.'
    return render(request, 'authentication/success-registration.html', {'text': text})


def login_view(request):
    """User login view"""
    context = {}

    if request.user and request.user.is_authenticated:
        return redirect('core:index')
    
    if request.method == "POST":
        form = LoginCustomUserModelForm(request.POST)
        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return  redirect('core:index')
    else:
        form = LoginCustomUserModelForm()

    context["form"] = form
    return render(request, 'authentication/login.html', context)


@login_required
def logout_view(request):
    """User logout view"""
    if request.method == 'POST':
        logout(request)
        return redirect('authentication:login')
    else:
        raise Http404
