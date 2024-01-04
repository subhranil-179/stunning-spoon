from django.urls import path
from article.views import home, detail, category

app_name = "article"

urlpatterns = [
    path("", home, name="home"),
    path("category/<str:name>", category, name="category"),
    path("article/<int:pk>", detail, name="detail")
]
