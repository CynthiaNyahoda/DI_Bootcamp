from django.shortcuts import render,redirect, get_object_or_404
from phonenumber_field.formfields import PhoneNumberField
from .forms import SearchForm
from .models import Person

# Create your views here.

def person_by_phonenumber(request, phone_number):
    person = get_object_or_404(Person, phone_number=phone_number)
    return render(request, 'phonebookapp/person_detail.html', {'person': person})

def person_by_name(request, name):
    persons = Person.objects.filter(name__icontains=name)
    return render(request, 'phonebookapp/person_list.html', {'persons': persons})


def search_person(request):
    if request.method == 'POST':
        search_term = request.POST.get('search_term')
        if search_term.isdigit():
            return redirect('phonebookapp:person_by_phonenumber', phone_number=search_term)
        else:
            return redirect('phonebookapp:person_by_name', name=search_term)
    else:
        form = SearchForm()
    return render(request, 'phonebookapp/search_person.html', {'form': form})
