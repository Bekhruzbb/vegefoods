from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .forms import CommentForm
from django.core.paginator import Paginator

# Create your views here.


def show_blog_page(request):
    categories = models.Category.objects.all()
    blog_articles = models.BlogItem.objects.all()
    tags = models.BlogTag.objects.all()
    context = {
        'blog_articles': blog_articles,
        'tags': tags,
        'categories': categories
    }
    for category in categories:
        category.count = blog_articles.filter(Category=category).count()

    return render(request, 'blog/blog.html', context)


def show_articles_by_category_page(request, slug):
    current_category = models.Category.objects.get(slug=slug)
    filter_articles = models.BlogItem.objects.filter(Category__slug=slug)

    categories = models.Category.objects.all()
    tags = models.BlogTag.objects.all()
    articles = models.BlogItem.objects.all()
    context = {
        'categories': categories,
        'blog_articles': filter_articles,
        'current_category': current_category,
        'tags': tags,
        'articles': articles
    }
    return render(request, 'blog/blog.html', context)


def show_articles_by_tag(request, slug):
    current_tags = models.BlogTag.objects.get(slug=slug)
    filter_tags = models.BlogItem.objects.filter(Tag__slug=slug)

    categories = models.Category.objects.all()
    tags = models.BlogTag.objects.all()
    context = {
        'blog_articles': filter_tags,
        'categories': categories,
        'current_tags': current_tags,
        'tags': tags
    }
    return render(request, 'blog/blog.html', context)


def show_blog_detail(request, slug):
    blog_articles = get_object_or_404(models.BlogItem, Slug=slug)
    categories = models.Category.objects.all()
    tags = models.BlogTag.objects.all()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Article = blog_articles
            comment.Author = request.user
            comment.save()
            return redirect('blog:detail', slug=slug)
    else:
        form = CommentForm()

    context = {
        'blog_articles': blog_articles,
        'form': form,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'blog/blog-item.html', context)


from django.db.models import Q


def search_blog(request):
    query = request.GET.get('q')
    if not query:
        blog_articles = models.BlogItem.objects.all()
    else:
        blog_articles = models.BlogItem.objects.filter(Q(Title__iregex=query))
    context = {
        'query': query,
        'blog_articles': blog_articles
    }
    return render(request, 'blog/search.html', context)
