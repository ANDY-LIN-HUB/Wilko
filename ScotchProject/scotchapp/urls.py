from django.urls import path
from . import views

# урлы для страниц сайта
urlpatterns = [
    path('', views.index)
]
