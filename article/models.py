from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField


class Article(models.Model):
    autor = models.ForeignKey(User, on_delete=models.PROTECT)

    data_publicacao = models.DateTimeField(default=timezone.now)
    data_edicao = models.DateTimeField(auto_now=True)

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)

    banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    texto = MarkdownxField()

    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titulo)
            slug = base_slug
            count = 1
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

        
