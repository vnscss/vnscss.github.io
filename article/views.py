from django.shortcuts import render
from .models import Article
from django.shortcuts import get_object_or_404


def get_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.views += 1
    article.save()
    return render(request, 'article/article.html', {'article': article})