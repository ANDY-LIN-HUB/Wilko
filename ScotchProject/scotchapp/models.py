from django.db import models


# модель категорий в админке, вводим их наименования
class Category(models.Model):
    name = models.CharField('Категория', max_length=100)

    def __str__(self):
        return self.name

    # меняет название модели
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# модель самих товаров с привязкой к классу выше
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    composition = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

