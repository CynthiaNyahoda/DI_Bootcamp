from django import forms
from RentaBike.models import branches


class branchform(forms.ModelForm):
    class Meta:
        model = branches
        fields = "__all__"