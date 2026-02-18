from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug': ('Title',)}
    list_display = ['id', 'Title', 'created_at']
    list_display_links = ['Title']


class ProductPhotoInline(admin.TabularInline):
    model = models.ProductPhoto
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug': ('Title',)}
    list_display = ['Title', 'created_at', 'Quantity', 'Status', 'Sale_percent']
    list_display_links = ['Title']
    inlines = [ProductPhotoInline]
    ordering = ['created_at']


@admin.register(models.RelatedProducts)
class RelatedProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'Title']
    list_display_links = ['Title']