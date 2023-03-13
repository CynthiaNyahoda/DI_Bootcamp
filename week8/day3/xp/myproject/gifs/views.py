from django.shortcuts import render, redirect, get_object_or_404
from .models import Gif, Category
from .forms import GifForm, CategoryForm


# Create your views here.


def homepage(request):
    gifs = Gif.objects.all()
    return render(request, 'gifs/homepage.html', {'gifs': gifs})

def add_gif(request):
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = GifForm()
    return render(request, 'gifs/add_gif.html', {'form': form})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request, 'gifs/add_category.html', {'form': form})

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    gifs = category.gif_set.all()
    return render(request, 'gifs/category.html', {'category': category, 'gifs': gifs})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'gifs/categories.html', {'categories': categories})

def gif(request, gif_id):
    gif = get_object_or_404(Gif, pk=gif_id)
    return render(request, 'gifs/gif.html', {'gif': gif})

    
