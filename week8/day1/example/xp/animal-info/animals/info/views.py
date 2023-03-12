from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Animal, Family
from .serializer import AnimalSerializer, FamilySerializer
# Create your views here.



class FamilyView(APIView):
    def get(self, request, id):
        family = Family.objects.get(pk=id)
        animals = family.animal_set.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)

class AnimalView(APIView):
    def get(self, request, id):
        animal = Animal.objects.get(pk=id)
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)
