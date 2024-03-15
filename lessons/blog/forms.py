from django import forms
from django.utils import timezone

from .models import Author


class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'})
    )
    bio = forms.CharField(widget=forms.Textarea)
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )


class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    is_published = forms.BooleanField()

