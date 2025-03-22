from django.db import models
from django.contrib.auth.models import User

from apps.authentication.models import CustomUser


class Category(models.Model):
    name = models.CharField("Название", max_length=255)
    icon = models.ImageField("categories_image/", null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['id', ]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):

    name = models.CharField("Название", max_length=255)
    image = models.ImageField("Фотография", upload_to='img/products')
    initial_price = models.IntegerField("Цена", default=0)
    description = models.TextField("Описание", null=True)
    end_time = models.DateTimeField("Конец", null=True)
    auction = models.BooleanField("Аукцион", default=False)
    category = models.ForeignKey(Category, models.RESTRICT, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    
    @property
    def prices(self):
        return Price.objects.filter(product=self).order_by('-date')

    @property
    def initial_price_format(self):
        return '{:7,.1f}'.format(self.initial_price)

    def __str__(self):
        return self.name


class Price(models.Model):

    product = models.ForeignKey(Product, on_delete=models.RESTRICT, verbose_name="Продукт")
    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT, verbose_name="Пользователь")
    price = models.IntegerField("Цена", default=0)
    date = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        ordering = ['id',]
        verbose_name = "Цена"
        verbose_name_plural = "Цены"
    
    @property
    def price_format(self):
        return '{:7,.1f}'.format(self.price)

    def __str__(self):
        return f"{self.price} from {self.user} for {self.product}"


class SoldProduct(models.Model):
    by = models.ForeignKey(CustomUser, models.RESTRICT)
    product = models.ForeignKey(Product, models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Sold Product"
        verbose_name_plural = "Sold Product"
