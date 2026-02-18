from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.BlogItem)
class BlogItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug': ('Title', )}

    list_display = ['id', 'created_at', 'Title']
    list_display_links = ['Title']


@admin.register(models.BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'Author', 'created_at']
    list_display_links = ['created_at', 'id']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category',)}
    list_display = ['id', 'category']
    list_display_links = ['category']