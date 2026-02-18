from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.show_blog_page, name='blog'),
    path('blog/search/', views.search_blog, name='search'),
    path('blog/<slug:slug>/', views.show_blog_detail, name='detail'),
    path('blog/categories/<slug:slug>/', views.show_articles_by_category_page, name='category'),
    path('tags/<slug:slug>/', views.show_articles_by_tag, name='tag')
]
