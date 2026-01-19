from django import forms
from .models import NewsArticles

class NewsArticlesForm(forms.ModelForm):
    class Meta:
        model = NewsArticles
        fields = '__all__'
        widgets = {
            'articleId': forms.NumberInput(attrs={'class': 'form-control'}),
            'articleImg': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'articleName': forms.TextInput(attrs={'class': 'form-control'}),
            'articleContent': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'publishDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'authorId': forms.NumberInput(attrs={'class': 'form-control'}),
        }
