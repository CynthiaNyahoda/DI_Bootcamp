from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Person

def search_by_phone(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        try:
            person = Person.objects.get(phone_number=phone_number)
            return render(request, 'person_detail.html', {'person': person})
        except Person.DoesNotExist:
            return render(request, 'person_not_found.html')
    else:
        return render(request, 'search_by_phone.html')

def search_by_name(request):
    if request.method == 'POST':
        name = request.POST['name']
        try:
            person = Person.objects.get(name=name)
            return render(request, 'person_detail.html', {'person': person})
        except Person.DoesNotExist:
            return render(request, 'person_not_found.html')
    else:
        return render(request, 'search_by_name.html')
