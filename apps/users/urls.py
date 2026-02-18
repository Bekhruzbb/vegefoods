from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('auth/', views.auth_page, name='auth'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_user, name='login'),
    path('reg_user/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout'),
    path('wishlist/', views.wishlist_page, name='wishlist'),
    path('wishlist/<str:product_id>/', views.add_or_delete, name='wishlist-action')
]
