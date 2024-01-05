from django.shortcuts import render, redirect

from article.forms import CommentForm
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
    comment_form = CommentForm()
    context = {
            "article": article,
            "comment_form": comment_form,
    }
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect(article)
        context.update({"comment_form": comment_form})

    return render(request, "article/detail.html", context)


def category(request, name):
    category_name = Category.objects.get(name=name).name
    category_articles = Category.objects.get(name=name).article_set.all()
    context = {
            "category_name": category_name,
            "articles": category_articles,
    }
    return render(request, "article/category.html", context)
