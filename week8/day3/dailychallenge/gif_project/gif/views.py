from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Gif

def gif_detail(request, gif_id):
    gif = get_object_or_404(Gif, pk=gif_id)

    if request.method == 'POST':
        if 'like' in request.POST:
            gif.likes += 1
        elif 'dislike' in request.POST:
            gif.likes -= 1
        gif.save()

        data = {
            'likes': gif.likes,
        }
        return JsonResponse(data)

    return render(request, 'gif_detail.html', {'gif': gif})

