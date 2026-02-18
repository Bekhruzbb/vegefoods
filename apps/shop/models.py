from django.db import models
from apps.common.models import BaseModel

# Create your models here.


class Products(BaseModel):
    Title = models.CharField(verbose_name='Название')
    Price = models.CharField(verbose_name='Цена продукта')
    Sale_percent = models.IntegerField(verbose_name='Процент скидки', default=0)
    Preview = models.ImageField(upload_to='shops/preview', null=True, blank=True)
    Slug = models.SlugField(unique=True, max_length=150)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(BaseModel):
    Title = models.CharField(verbose_name='Название')
    Slug = models.SlugField(max_length=150, verbose_name='Краткая ссылка', unique=True)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Product(BaseModel):
    class SizeChoices(models.TextChoices):
        SMALL = 'small', 'Small'
        MEDIUM = 'medium', 'Medium'
        LARGE = 'large', 'large'
        EXTRA_LARGE = 'extra_large', 'Extra_large'

    class StatusChoices(models.TextChoices):
        SOLD = 'sold', 'Sold'
        NEW = 'new', 'New'
        IN_STOCK = 'in stock', 'In stock'

    Title = models.CharField(verbose_name='Краткое название')
    Price = models.IntegerField(verbose_name='Цена продукта')
    Preview = models.ImageField(upload_to='shop/products/preview/', verbose_name='Фото', null=True)
    Sale_percent = models.IntegerField(verbose_name='Процент скидки', default=0)
    Short_description = models.TextField()
    Slug = models.SlugField(max_length=150, verbose_name='Краткая ссылка', unique=True)
    Quantity = models.IntegerField('Кол-во', default=0)
    Size = models.CharField(choices=SizeChoices.choices, null=True, blank=True, verbose_name='Размер продуктов')
    Status = models.CharField(choices=StatusChoices.choices, null=True, blank=True, verbose_name='Статус продукта')
    Sold = models.IntegerField(verbose_name='Проданные товары', default=0)
    category = models.ManyToManyField(Category, related_name='categories')

    def get_price(self):
        if (self.Status == 'new' or self.Status == 'in stock') and self.Sale_percent:
            price = round(float(self.Price) - (float(self.Price * (self.Sale_percent / 100))))
            return price
        return self.Price

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Страница продукта'
        verbose_name_plural = 'Страницы продукта'


class ProductPhoto(BaseModel):
    Title = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='заголовок')
    image = models.ImageField(upload_to='shop/images/', verbose_name='Фото продукта')

    class Meta:
        verbose_name = 'Фото продукта'


class RelatedProducts(BaseModel):
    Title = models.CharField(verbose_name='Заголовок')
    Text = models.TextField(verbose_name='Текст')



