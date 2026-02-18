from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import logout, login, authenticate
from .models import Favorite, UserCustomUser
from apps.shop.models import Product
# Create your views here.


def register_page(request):
    register_form = RegisterForm()
    context = {
        'register_form': register_form
    }

    return render(request, 'users/register.html', context)


def auth_page(request):
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    return render(request, 'users/auth.html', context)


def login_user(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        if user:
            login(request, user)
            return redirect('main:home')
    else:
        form = LoginForm()


def register_user(request):
    form = RegisterForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('users:auth')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('main:home')


def add_or_delete(request, product_id):
    favourite, create = Favorite.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=product_id)
    if product in favourite.product.all():
        favourite.product.remove(product_id)
    else:
        favourite.product.add(product_id)

    return redirect('users:wishlist')


def wishlist_page(request):
    favourite, create = Favorite.objects.get_or_create(user=request.user)
    context = {
        'favourite': favourite
    }
    return render(request, 'users/wishlist.html', context)


