from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage', views.homepage, name='homepage'),
    path('adddirector', views.addDirector, name='adddirector'),
    path('addfilm', views.addFilm, name='addfilm'),
    
]
