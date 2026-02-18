from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('shop/', views.show_shop_page, name='shop'),
    path('shop/category/<slug:slug>/', views.show_products_by_category, name='category'),
    path('shop/product/<slug:slug>/', views.show_product_detail, name='product')
]
