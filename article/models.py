from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def get_absolute_url(self):
        return reverse("article:category", kwargs={"name": self.name})

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    title = models.CharField(unique=True, max_length=150)
    body = models.TextField()
    description = models.CharField(max_length=500, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    category = models.ManyToManyField(Category)

    def get_absolute_url(self):
        return reverse("article:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.CharField(max_length=1024)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
