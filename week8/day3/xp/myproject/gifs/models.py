from django.db import models
from django.utils import timezone

class Gif(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    uploader_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    gifs = models.ManyToManyField(Gif)

    def __str__(self):
        return self.name
