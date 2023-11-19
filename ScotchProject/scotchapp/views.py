from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


def index(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'scotchapp/index.html', context)