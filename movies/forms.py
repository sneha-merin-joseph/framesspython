from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'category', 'title', 'minutes', 'seconds', 'director', 'stars', 
            'writers', 'description', 'detailed_description', 'image', 
            'website_url', 'status', 'releas_date'
        ]
        widgets = {
            'releas_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['subject', 'comment', 'rate']
