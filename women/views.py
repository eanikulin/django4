from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.template.loader import render_to_string

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


data_db = [
    {"id": 1, "title": "Анджелина Джоли", "content": "Биография Анджелины", "is_published": True},
    {"id": 2, "title": "Петрова Оля", "content": "Биография Оли", "is_published": False},
    {"id": 3, "title": "Лобкова Катя", "content": "Биография Кати", "is_published": True},
]


def index(request):
    # t = render_to_string("women/index.html")
    # return HttpResponse(t)
    data = {
        "title": "главная страница",
        "menu": menu,
        "float": 30.1,
        "lst": [1, "fdg", True],
        "set": {1, 2, 3, 5},
        "dict": {"key1": "value1", "key2": "value2"},
        "obj": MyClass(10, 20),
        "url": slugify("The main page"),
        "posts": data_db,
    }
    return render(request, "women/index.html", context=data)


def about(request):
    return render(request, "women/about.html", {"title": "О сайте"})


def categories(request, cat_id):
    return HttpResponse(f"<h1>Категории</h1> <p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Категории</h1> <p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2022:
        # return redirect('/', permanent=True)
        # return redirect(index)
        # return redirect("home")
        # return redirect("cats", "music")
        uri = reverse("cats", args=("music",))
        # return redirect(uri)
        return HttpResponseRedirect(uri)
    if year > 2024:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1> <p>Год: {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<p>Страница не найдена</p>")
