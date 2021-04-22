from django.db import models
from django.core.validators import MinValueValidator


# Создаём модель товара
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True,)  # названия товаров не должны повторяться
    price = models.FloatField(validators=[MinValueValidator(0.0, 'Price should be >= 0.0')])
    quantity = models.IntegerField(validators=[MinValueValidator(0, 'Quantity should be >= 0')])
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products', )

    description = models.TextField()

    def __str__(self):
        return f'{self.name} {self.quantity}'

    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с товаром
        return f'/products/{self.id}'


    #  создаём категорию, к которой будет привязываться товар
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # названия категорий тоже не должны повторяться

    def __str__(self):
        return f'{self.name}'