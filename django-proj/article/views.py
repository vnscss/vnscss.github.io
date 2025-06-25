from django.shortcuts import render
from .models import Article
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.db.models import Q
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse


def get_article(request, slug):
    slug = slug.replace('.html', '')
    article = get_object_or_404(Article, slug=slug)
    article.views += 1
    article.save()
    return render(request, 'article/article.html', {'article': article})

def mainPage(request):
    articles = Article.objects.order_by('-data_publicacao')[:5]
    return render(request, 'mainPage.html', {'articles': articles})

class ArticletListView(ListView):
    paginate_by = 10
    model = Article

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Article.objects.filter(
                Q(titulo__icontains=query) |
                Q(chamada__icontains=query) |
                Q(texto__icontains=query)
            )
        return super().get_queryset()


def manual_error_404(request):
    return render(request, '404.html')


def error_404(request, exception):
    return render(request, '404.html')


def get_all_articles(request):
    slugs = Article.objects.values_list('slug', flat=True)
    response = "\n".join(f"{slug}.html" for slug in slugs)
    return HttpResponse(response, content_type="text/plain")