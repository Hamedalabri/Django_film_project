from django import forms
from .models import Film, Category

class FilmForm(forms.ModelForm):
   

    class Meta:
        model = Film
        fields = ['title', 'description', 'author', 'year', 'category']
        widgets ={
            'category' : forms.Select(attrs={'class': 'form-control'}),
        }

    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']    
