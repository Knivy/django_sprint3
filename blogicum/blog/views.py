from datetime import datetime as dt  # type: ignore[import-untyped]

from django.shortcuts import get_object_or_404  # type: ignore[import-untyped]
from django.shortcuts import render  # type: ignore[import-untyped]
from django.http import HttpResponse  # type: ignore[import-untyped]
from django.db.models import QuerySet  # type: ignore[import-untyped]

from .models import Category, Post


def index(request) -> HttpResponse:
    """Главная страница."""
    template: str = 'blog/index.html'
    post_list: QuerySet = (Post.objects.select_related('author', 'category')
                           .filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=dt.now(),
    )[:5])
    context: dict = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id) -> HttpResponse:
    """Отдельный пост."""
    template: str = 'blog/detail.html'
    post: QuerySet = get_object_or_404(Post.objects.select_related(
        'author',
        'category'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=dt.now(),
    ), pk=id)
    context: dict = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug) -> HttpResponse:
    """Категория постов."""
    template: str = 'blog/category.html'
    category: Category = get_object_or_404(Category.objects.filter(
        is_published=True,
    ),
        slug=category_slug)
    post_list: QuerySet = (Post.objects
                           .select_related('author', 'category')
                           .filter(
                               is_published=True,
                               pub_date__lte=dt.now(),
                               category=category,
                           ))
    context: dict = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template, context)
