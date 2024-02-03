from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def index(request):
    return HttpResponse("Страница приложения")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Категории</h1> <p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Категории</h1> <p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2024:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1> <p>Год: {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<p>Страница не найдена</p>")

