from django import forms
from .models import Film, Director

class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'release_date', 'created_in_country', 'available_in_countries', 'category', 'director']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['first_name', 'last_name']