from django import forms
from datetime import date
from .models import Images
import warnings

class ImageForm(forms.ModelForm): 

    class Meta: 
        model = Images 
        fields = ['name', 'image'] 

class SubmitEmbed(forms.Form):
    url = forms.URLField()