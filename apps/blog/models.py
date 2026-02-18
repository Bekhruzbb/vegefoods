from django.db import models
from apps.common.models import BaseModel
# Create your models here.


class Category(BaseModel):
    category = models.CharField(verbose_name='Имя категории',null=True, blank=True, unique=True)
    slug = models.SlugField(unique=True, verbose_name='Короткая ссылка')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class BlogTag(BaseModel):
    name = models.CharField(unique=True, verbose_name='Тег')
    slug = models.SlugField(unique=True, verbose_name='Короткая ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class BlogItem(BaseModel):
    Title = models.CharField(max_length=30, verbose_name='Заголовок')
    Slider = models.ImageField(upload_to='blog/slider/', verbose_name='Слайд')
    Short_description = models.CharField(max_length=40, verbose_name='Краткое описание')
    Full_description = models.TextField(verbose_name='полное описание')
    Image = models.ImageField(upload_to='blog/images/', verbose_name='Фото', null=True)
    Tag = models.ManyToManyField(BlogTag, related_name='tags', verbose_name='Тэг')
    Slug = models.SlugField(unique=True, verbose_name='Короткая ссылка')
    Author = models.CharField(max_length=20, verbose_name='Автор статьи')
    Category = models.ManyToManyField(Category, related_name='blog_items', verbose_name='Имя категории')

    def __str__(self):
        return self.Author

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(BaseModel):
    Author = models.ForeignKey('users.UserCustomUser',
                               on_delete=models.CASCADE, verbose_name='Автор', related_name='comments')
    Article = models.ForeignKey(BlogItem, on_delete=models.CASCADE, verbose_name='Статья', related_name='comments')
    Email = models.EmailField(max_length=20, null=True)
    Website = models.CharField(null=True)
    Text = models.TextField(verbose_name='Текст коммента', null=True)

    def __str__(self):
        return f"{self.Author} - {self.Article}"

    class Meta:
        verbose_name = 'Комментарии'


