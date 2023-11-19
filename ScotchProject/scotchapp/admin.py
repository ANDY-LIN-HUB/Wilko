from django.contrib import admin
from .models import Category, Product

# регистрируем модели в админке
admin.site.register(Category)
admin.site.register(Product)