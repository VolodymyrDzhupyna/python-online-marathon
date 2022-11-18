from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout


def sign_up(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        extra_fields = {
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'role': int(role),
            'is_active' : True
        }
        if role == '0':
            object_custom_user = CustomUser.objects.create_user(email, password, **extra_fields)

        if role == '1':
            object_custom_user = CustomUser.objects.create_user(email, password, **extra_fields)

        context['object'] = object_custom_user
        context['created'] = True
    return render(request, 'authentication/signup.html', context=context)

def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is None:
            context = {'error': 'Invalid username or password'}
            return render(request, 'authentication/login.html', context)
        login(request, user)
        return redirect('/')
    return render(request, 'authentication/login.html', {})

def log_out(request):
    logout(request)
    return redirect('/')

def show_all(request):
    users = CustomUser.get_all()
    context = {
        'users' : users,
    }
    return render(request, 'authentication/all.html', context)

def show_one(request):
    context = {}
    if request.method == 'POST':
        id = request.POST.get('id')
        user = CustomUser.get_by_id(id)
        orders = user.order_set.select_related()
        books = [order.book for order in orders]
        context['user_searched'] = user
        context['orders'] = orders
        context['books'] = books
    return render (request, 'authentication/one.html', context)

def home(request):
    return render(request, 'authentication/home.html')