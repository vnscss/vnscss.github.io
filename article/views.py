from django.shortcuts import render
from .models import Article
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.db.models import Q


def get_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.views += 1
    article.save()
    return render(request, 'article/article.html', {'article': article})

def mainPage(request):
    articles = Article.objects.order_by('-data_publicacao')[:5]
    return render(request, 'mainPage.html', {'articles': articles})

class ArticletListView(ListView):
    paginate_by = 2
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
