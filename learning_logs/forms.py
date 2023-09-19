from django import forms
from .models import Topic
class PersonForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['text']
        labels={"text":''}