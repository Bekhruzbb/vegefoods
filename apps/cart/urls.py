from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.show_cart_page, name='cart'),
    path('add/<str:product_id>/<int:quantity>/', views.add_delete_cart, name='add-to-cart'),
    path('checkout/', views.show_checkout_page, name='checkout')
]