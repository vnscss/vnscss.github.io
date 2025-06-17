from django.shortcuts import render
from .models import Article
from django.shortcuts import get_object_or_404


def get_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'teste.html', {'article': article})