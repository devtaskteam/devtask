# Create your views here.
from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'Просмотр авторизации через соцсети',
    }
    return render(request, 'social.html', context)
