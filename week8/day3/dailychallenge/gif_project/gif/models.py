from django.db import models

# Create your models here.
from django.db import models

class Gif(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    likes = models.IntegerField(default=0)
