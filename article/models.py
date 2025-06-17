from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from django.utils.text import slugify
from markdownx.utils import markdownify


class Article(models.Model):
    autor = models.ForeignKey(User, on_delete=models.PROTECT)

    data_publicacao = models.DateTimeField(default=timezone.now)
    data_edicao = models.DateTimeField(auto_now=True)

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True) 

    chamada = models.TextField(blank=True)

    banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    texto = MarkdownxField()

    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titulo)
            slug = base_slug
            counter = 1
            # Ensure uniqueness
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)
    
    @property
    def texto_html_parse(self):
        return markdownify(self.texto)

    def __str__(self):
        return self.titulo

        
