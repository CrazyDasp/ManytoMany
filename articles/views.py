from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.prefetch_related('tags')  # Получаем все статьи с предварительно загруженными тегами
    context = {'articles': articles}
    return render(request, template, context)
