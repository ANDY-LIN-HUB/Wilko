from django.shortcuts import render
from django.conf import settings
from .models import MenuItem


def index(request):
    context = {}
    for t in MenuItem.TYPE:
        context[f'menu_{t[0]}'] = MenuItem.objects.filter(type__exact=t[0])

    return render(request, 'scotchapp/index.html', context)