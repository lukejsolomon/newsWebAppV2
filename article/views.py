from django.shortcuts import render, get_object_or_404
from .models import *


def allArticles(request):
    articles = Article.objects.filter(type="news").order_by("-date")[:3]
    featured = Article.objects.filter(type="feat").order_by("-date")
    podcasts = Article.objects.filter(type="pod").order_by("-date")[:3]
    contributors = Article.objects.filter(type="pro")[:5]
    return render(request, 'article/allArticles.html', {'articles': articles, 'featured': featured, 'podcasts': podcasts, 'contributors': contributors})


def articlePage(request, blog_id):
    article = get_object_or_404(Article, pk=blog_id)
    return render(request, 'article/articlePage.html', {'article': article})


def news(request):
    articles = Article.objects.filter(type="news").order_by("-date")
    return render(request, 'article/news.html', {'news': articles})


def podcasts(request):
    articles = Article.objects.filter(type="pod").order_by("-date")
    return render(request, 'article/podcasts.html', {'articles': articles})


def podcastPage(request, blog_id):
    article = get_object_or_404(Article, pk=blog_id)
    return render(request, 'article/articlePage.html', {'article': article})


def contributors(request):
    articles = Article.objects.filter(type="pro")
    return render(request, 'article/contributors.html', {'articles': articles})


def contributorsPage(request, blog_id):
    article = get_object_or_404(Article, pk=blog_id)
    return render(request, 'article/contributorsPage.html', {'article': article})
