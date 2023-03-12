from django.urls import path
from .views import AnimalView, FamilyView

urlpatterns = [
    path('family/<int:id>/', FamilyView.as_view()),
    path('animal/<int:id>/', AnimalView.as_view()),
]
