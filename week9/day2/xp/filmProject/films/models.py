from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

# Create your models here.
class User(AbstractUser, PermissionsMixin):
    pass
class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    
    
class Film(models.Model):
    title = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    release_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=50)

    class Meta:
        permissions = [
            ("edit_film", "Can edit film data"),
        ]






    
    
