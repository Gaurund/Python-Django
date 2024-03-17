from django import forms
from django.utils import timezone

from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=16, decimal_places=2)
    quantity = forms.IntegerField()
    was_added = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
