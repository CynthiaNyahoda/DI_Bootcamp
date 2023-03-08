from django.urls import path
from .views import gif_detail, popular_gifs

urlpatterns = [
    path('gifs/<int:gif_id>/', gif_detail, name='gif_detail'),
    path('popular-gifs/', popular_gifs, name='popular_gifs'),
]
