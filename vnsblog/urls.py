"""
URL configuration for vnsblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from markdownx.views import ImageUploadView, MarkdownifyView
from article.views import *

urlpatterns = [
    path('' , mainPage , name='mainPage'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("markdownx/upload/", login_required(ImageUploadView.as_view()), name="markdownx_upload"),
    path("markdownx/markdownify/", login_required(MarkdownifyView.as_view()), name="markdownx_markdownify"),
] 

article = [
    path('article/<slug:slug>', get_article , name='get_article'),
    path('my-articles/' , ArticletListView.as_view() , name='ArticleListView' )
]

urlpatterns += article
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

