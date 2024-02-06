from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):
    # t = render_to_string("women/index.html")
    # return HttpResponse(t)
    data = {
        "title": "Главная страница",
        "menu": menu,
        "float": 23.7,
        "lst": [1, "fdg", True],
        "set": {1, 2, 3, 5},
        "dict": {"key1": "value1", "key2": "value2"},
        "obj": MyClass(10, 20),
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
