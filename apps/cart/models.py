from django.db import models
from apps.common.models import BaseModel


# Create your models here.


class Order(BaseModel):
    user = models.OneToOneField('users.UserCustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.user} cart'

    def get_cart_price_without_sale(self):
        return sum([i.get_cart_price_without_sale() for i in self.cart_products.all()])

    def get_cart_total_price(self):
        return sum([i.get_total_price() for i in self.cart_products.all()])

    def get_cart_total_quantity(self):
        return sum([i.Quantity for i in self.cart_products.all])

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(BaseModel):
    cart = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cart_products', verbose_name='Корзина')
    product = models.ForeignKey('shop.Product', on_delete=models.SET_NULL, verbose_name='Продукт', null=True)
    quantity = models.IntegerField(verbose_name='Кол-во')

    def get_cart_price_without_sale(self):
        return (self.product.Sale_percent / 100) * self.product.Price

    def get_total_price(self):
        return self.product.get_price()

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Billing(BaseModel):
    First_name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    State = models.CharField(max_length=40)
    Street_address = models.CharField()
    City = models.CharField(max_length=30)
    Zip = models.IntegerField()
    phone = models.IntegerField()
    email_address = models.EmailField()
