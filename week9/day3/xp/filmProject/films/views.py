from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddFilmForm, AddDirectorForm
from django.contrib import messages
from .models import Film, Comment
from .forms import CommentForm


def film_detail(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    comments = Comment.objects.filter(film=film)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.film = film
            comment.save()
            messages.success(request, 'Your comment was added successfully.')
            return redirect('film_detail', film_id=film_id)
    else:
        form = CommentForm()

    context = {
        'film': film,
        'comments': comments,
        'form': form,
    }
    return render(request, 'film_detail.html', context)


def homepage(request):
    return render(request,'homepage.html')

def addFilm(request):
    if request.method == 'POST':
        form = AddFilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddFilmForm()
        return render(request, 'film/addfilm.html',{'form': form})
    
    
def addDirector(request):
    if request.method == 'POST':
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = AddDirectorForm()
    return render(request, 'director/adddirector.html', {'form': form})
            