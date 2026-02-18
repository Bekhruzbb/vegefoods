from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['created_at']


@admin.register(models.InstagramPhoto)
class InstagramPhotoAdmin(admin.ModelAdmin):
    list_display = ['Title', 'created_at']
    list_display_links = ['Title']


@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'title']
    list_display_links = ['title']


@admin.register(models.BestPrice)
class BestPriceAdmin(admin.ModelAdmin):
    list_display = ['id', 'Title', 'created_at']
    list_display_links = ['created_at']


@admin.register(models.PostSlider)
class PostSliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']


@admin.register(models.PreSlider)
class PreSliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'Text', 'created_at']
    list_display_links = ['Text', 'created_at']


@admin.register(models.Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['created_at']