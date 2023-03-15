from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Animal, Family
from .serializers import AnimalSerializer, FamilySerializer
from .forms import CustomerForm


def index(request):

	form = CustomerForm()

	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'index.html', context)



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

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'info/animal_list.html', {'animals': animals})
# Create your views here.
