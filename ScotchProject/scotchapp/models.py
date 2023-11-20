from django.db import models


# модель категорий в админке, вводим их наименования
class MenuItem(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to='images')
    title = models.CharField(max_length=80, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена')
    description = models.TextField(max_length=120, default=0, verbose_name='Состав')

    TYPE = [
        ('eat', 'Закуски'),
        ('soup', 'Супы'),
        ('pizza', 'Пицца'),
        ('pasta', 'Паста'),
        ('sandwitch', 'Сэндвичи'),
        ('hot', 'Горячие блюда'),
        ('desert', 'Десерты'),
        ('drinks', 'Напитки'),
        ('sous', 'Соусы'),
        ('salat', 'Салаты')
    ]

    type = models.CharField(choices=TYPE, max_length=15, default='eat', verbose_name='Категория')

    def __str__(self):
        return self.title
    

