from django.shortcuts import render, redirect
from .forms import AddFilmForm, AddDirectorForm

# Create your views here.
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
            