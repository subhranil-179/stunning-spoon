from django.urls import path
from article.views import home, detail

app_name = "article"

urlpatterns = [
    path("", home, name="home"),
    path("article/<int:pk>", detail, name="detail")
]
