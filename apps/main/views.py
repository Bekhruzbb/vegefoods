from django.shortcuts import render
from . import models
from apps.cart.models import Order
# Create your views here.


def show_home_page(request):
    if request.user.is_authenticated:
        cart, created = Order.objects.get_or_create(user=request.user)

    slides = models.HomeSlider.objects.all()
    postslides = models.PostSlider.objects.all()
    features = models.Feature.objects.all()
    discounts = models.BestPrice.objects.all()
    testimonials = models.Testimonials.objects.all()
    context = {
        'slides': slides,
        'postslides': postslides,
        'features': features,
        'discounts': discounts,
        'testimonials': testimonials
    }

    return render(request, 'main/index.html', context)


def show_contacts(request):
    return render(request, 'main/contacts.html')


def show_about_page(request):
    return render(request, 'main/about.html')