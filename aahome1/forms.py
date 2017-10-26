from django import forms
from django.contrib.auth import authenticate
#from django.contrib.auth.models import User
from .models import Product




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ( 'name', 'product_image', 'category', 'desc', 'price', 'start_date', 'start_time',)


        
class SearchForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category',)
