from django.shortcuts import render, redirect
from .models import CartItem, Order
from apps.shop.models import Product
from .forms import BillingForm


# Create your views here.


def add_delete_cart(request, product_id, quantity):
    order, created = Order.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=product_id)
    if product in [i.product for i in order.cart_products.all()]:
        order_product = CartItem.objects.get(product=product)
        order_product.quantity += quantity
        product.Quantity -= quantity

        order_product.save()
        product.save()
    else:
        CartItem.objects.create(cart=order, quantity=quantity, product=product)
        product.Quantity -= quantity
        product.save()

        return redirect('cart:cart')


def show_cart_page(request):
    cart, created = Order.objects.get_or_create(user=request.user)
    context = {
        'cart': cart
    }

    return render(request, 'cart/cart.html', context)


def show_checkout_page(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart:checkout')
    else:
        form = BillingForm()
    cart, created = Order.objects.get_or_create(user=request.user)

    context = {
        'form': form,
        'cart': cart
    }
    return render(request, 'cart/checkout.html', context)
