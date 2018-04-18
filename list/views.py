from django.shortcuts import render
from string import ascii_uppercase
from home.models import Anime

alphabet = ascii_uppercase


def list(request):
    context = {'alphabet': alphabet}
    return render(request, 'list/list.html', context)


def list_detail(request, letter):
    anime = Anime.objects.filter(title__startswith=letter)
    context = {'anime': anime}
    return render(request, 'list/detail.html', context)


def ended(request):
    ended = Anime.objects.order_by('title')
    context = {'ended': ended}
    return render(request, 'list/ended.html', context)
