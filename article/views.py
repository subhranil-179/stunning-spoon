from django.shortcuts import render
from article.models import Article

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
