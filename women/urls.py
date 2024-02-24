from django.urls import (
    path,
    re_path,
    register_converter,
)

from . import (
    converters,
    views,
)

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path("", views.index, name="home"),
    path("cats/<int:cat_id>/", views.categories, name="cats_id"),
    path("about/", views.about, name="about"),
    path("cats/<slug:cat_slug>/", views.categories_by_slug, name="cats"),
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive)
    path("archive/<year4:year>/", views.archive, name="archive"),
    path("post/<int:post_id>/", views.show_post, name="post"),
    path("addpage/", views.addpage, name="add_page"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
]
