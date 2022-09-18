from django.views.generic import ListView
from django.shortcuts import render
from articles.models import Article, ArticleScope
from django.db.models import Prefetch


def articles_list(request):
    template = 'articles/news.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    articles = Article.objects.order_by(ordering).prefetch_related(
        Prefetch('scopes', queryset=ArticleScope.objects.select_related('topic').order_by('-is_main', 'topic')))
    context['object_list'] = articles

    return render(request, template, context)


# pr1 = Prefetch('rubrics', queryset=Relations.objects.select_related('rubric').order_by('-primary', 'rubric'))
# object_list = Article.objects.prefetch_related(pr1).order_by('-published_at')