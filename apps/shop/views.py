from django.shortcuts import render
from apps.shop.models import Category, Product, ProductPhoto
from django.core.paginator import Paginator
# Create your views here.


def show_shop_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'categories': categories,
        'products': products
    }

    return render(request, 'shop/shop.html', context)


def show_products_by_category(request, slug):
    current_category =(Category.objects.get(Slug=slug))
    products = Product.objects.filter(category__Slug=slug)

    categories = Category.objects.all()
    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'current_category': current_category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'shop/shop.html', context)


def show_product_detail(request, slug):
    product = Product.objects.get(Slug=slug)
    images = ProductPhoto.objects.filter(Title=product)
    products = Product.objects.all()
    category = product.category.all()
    context = {
        'product': product,
        'images': images,
        'category': category,
        'products': products
    }

    return render(request, 'shop/product_detail.html', context)