from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from .models import Film, Director
from star_ratings.models import Rating
from .forms import CommentForm



class Film(models.Model):
    title = models.CharField(max_length=255)
    # other fields...
    rating = Rating(
        verbose_name='Film rating',
        max_value=5,
        allow_anonymous=True,
        allow_delete=True,
    )



def film_detail(request, film_id):
    try:
        film = get_object_or_404(Film, id=film_id)
        comments = Comment.objects.filter(film=film)
    except Http404:
        return render(request, '404.html')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.film = film
            comment.save()
    else:
        form = CommentForm()
    
    context = {
        'film': film,
        'comments': comments,
        'form': form,
    }
    return render(request, 'film_detail.html', context)





@user_passes_test(lambda u: u.is_superuser)
def delete_film(request, film_id):
    film = Film.objects.get(id=film_id)
    film.delete()
    messages.success(request, f"{film.title} was deleted successfully.")
    return redirect('film_list')

@user_passes_test(lambda u: u.is_superuser)
def delete_director(request, director_id):
    director = Director.objects.get(id=director_id)
    director.delete()
    messages.success(request, f"{director.name} was deleted successfully.")
    return redirect('director_list')


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






    
    
