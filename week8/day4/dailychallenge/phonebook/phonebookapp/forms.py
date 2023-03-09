from django import forms
from phonenumber_field.formfields import PhoneNumberField

class SearchForm(forms.Form):
    search_term = forms.CharField(label='Search', max_length=255, required=True)
