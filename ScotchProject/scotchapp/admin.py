from django.contrib import admin
from .models import MenuItem

# регистрируем модели в админке
admin.site.register(MenuItem)