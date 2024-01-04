from django.shortcuts import render
from article.models import Article, Category

# Create your views here.


def home(request):
    articles = Article.objects.all()
    context = {
            "articles": articles
    }
    return render(request, "article/home.html", context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "article/detail.html", context)


def category(request, name):
    category_name = Category.objects.get(name=name).name
    category_articles = Category.objects.get(name=name).article_set.all()
    context = {
            "category_name": category_name,
            "articles": category_articles,
    }
    return render(request, "article/category.html", context)
