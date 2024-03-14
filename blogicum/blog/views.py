from django.shortcuts import render  # type: ignore[import-untyped]
from django.http import HttpResponseNotFound  # type: ignore[import-untyped]
from django.http import HttpResponse  # type: ignore[import-untyped]


def index(request) -> HttpResponse:
    """Главная страница."""
    template: str = 'blog/index.html'
    context: dict = {'posts': posts[::-1]}
    return render(request, template, context)


def post_detail(request, id) -> HttpResponse:
    """Отдельный пост."""
    template: str = 'blog/detail.html'
    context: dict = {}
    for post in posts:
        if post['id'] == id:
            context = {'post': post}
    if not context:
        raise HttpResponseNotFound('Страница не найдена.')
    return render(request, template, context)


def category_posts(request, category_slug) -> HttpResponse:
    """Категория постов."""
    template: str = 'blog/category.html'
    context: dict = {
        'category': category_slug,
    }
    return render(request, template, context)
