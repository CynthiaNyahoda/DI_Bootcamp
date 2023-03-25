from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .form import ImageForm
from .models import Image
from django.utils import timezone

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('images')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})


def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "index.html", {"obj": obj})
    else:
        form = ImageForm()
        img = Image.objects.order_by('-upload_date')
        return render(request, "index.html", {"img": img, "form": form})



from django.core.paginator import Paginator
from django.utils import timezone
from datetime import datetime

def image_list(request):
    if request.GET.get('start_date') and request.GET.get('end_date'):
        start_date = timezone.make_aware(datetime.strptime(request.GET['start_date'], '%Y-%m-%d'))
        end_date = timezone.make_aware(datetime.strptime(request.GET['end_date'], '%Y-%m-%d'))
        images = Image.objects.filter(upload_date__range=(start_date, end_date)).order_by('-upload_date')
    else:
        images = Image.objects.order_by('-upload_date')

    paginator = Paginator(images, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'image_list.html', {'page_obj': page_obj})

