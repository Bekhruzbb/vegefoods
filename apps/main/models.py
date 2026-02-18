from apps.common.models import BaseModel
from django.db import models


class HomeSlider(BaseModel):
    preview = models.ImageField(upload_to='slider/', verbose_name='Фото главной страницы')
    title = models.CharField(max_length=40, verbose_name='Заголовок')
    short_description = models.TextField(max_length=50, verbose_name='Краткое описание')

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class PreSlider(BaseModel):
    Title = models.CharField(max_length=30, verbose_name='Заголовок')
    Text = models.CharField(max_length=40, verbose_name='Текст')

    class Meta:
        verbose_name = 'Текст до слайда'
        verbose_name_plural = 'Текст до слайдов'


class InstagramPhoto(BaseModel):
    Subtitle = models.CharField(max_length=30, verbose_name='Текст до заголовка')
    Title = models.CharField(max_length=40, verbose_name='Заголовок')
    photo = models.ImageField(upload_to='instagram_photo/', verbose_name='Фото')


class BestPrice(BaseModel):
    Subtitle = models.CharField(max_length=30, verbose_name='Текст до заголовка')
    Title = models.CharField(max_length=40, verbose_name='Заголовок')
    Text = models.CharField(max_length=40, verbose_name='Текст')


class Testimonials(BaseModel):
    photo = models.ImageField(upload_to='testimonials/photo', verbose_name='Фото автора', null=True, blank=True)
    text = models.TextField(verbose_name='Текст')
    name = models.CharField(max_length=15, verbose_name='Имя')
    position = models.CharField(max_length=10, verbose_name='Текущая позиция')


class PostSlider(BaseModel):
    icon = models.ImageField(upload_to='slider/icon/', verbose_name='Иконка', null=True, blank=True)
    title = models.CharField(max_length=20, verbose_name='Заголовок')
    short_description = models.CharField(max_length=30, verbose_name='Краткое описание')


class Feature(BaseModel):
    title = models.CharField(max_length=20, verbose_name='Заголовок')
    short_description = models.CharField(max_length=30, verbose_name='Краткое описание')
