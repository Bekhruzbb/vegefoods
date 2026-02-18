from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.shop.models import Product
from apps.common.models import BaseModel
# Create your models here.


class UserCustomUser(AbstractUser):
    email = models.EmailField(verbose_name='Email', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Favorite(BaseModel):
    user = models.OneToOneField(UserCustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ManyToManyField(Product, verbose_name='продукт', related_name='favs')

