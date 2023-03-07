from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from people.models import Person

def people(request):
    people = Person.objects.order_by('age')
    return render(request, 'people/people.html', {'people': people})

def person_detail(request, id):
    person = get_object_or_404(Person, pk=id)
    return render(request, 'people/person_detail.html', {'person': person})
