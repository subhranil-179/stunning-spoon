from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(unique=True, max_length=150)
    body = models.TextField()
    description = models.CharField(max_length=500, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)

    def __str__(self):
        return self.title
