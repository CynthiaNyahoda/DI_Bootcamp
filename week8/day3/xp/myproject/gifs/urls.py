from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add-gif/', views.add_gif, name='add_gif'),
    path('add-category/', views.add_category, name='add_category'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('categories/', views.categories, name='categories'),
    path('gif/<int:gif_id>/', views.gif, name='gif'),
    
]

urlpatterns += staticfiles_urlpatterns()