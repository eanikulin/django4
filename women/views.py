from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Страница приложения")


def categories(request):
    return HttpResponse("<h1>Категории</h1>")
