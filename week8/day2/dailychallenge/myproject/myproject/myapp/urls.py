from django.urls import path
from . import views

urlpatterns = [
    path('person/phonenumber/', views.search_by_phone, name='search_by_phone'),
    path('person/name/', views.search_by_name, name='search_by_name'),
]

