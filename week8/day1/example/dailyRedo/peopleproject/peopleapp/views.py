from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Person

def people_list(request):
    people = Person.objects.order_by('age')
    return render(request, 'people_list.html', {'people': people})

def person_detail(request, id):
    person = get_object_or_404(Person, pk=id)
    return render(request, 'person_detail.html', {'person': person})
