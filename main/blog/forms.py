# This is how i add a class to every field from models.py and add it to DOM

from django import forms
from .models import Post, Category

categories = Category.objects.all().values_list('name', 'name')

category_list = []

for item in categories:
    category_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ( "title", "author", "category", "body", "slug")

        widgets = {
            'title': forms.TextInput(attrs={"class": 'uk-input uk-form-small uk-form-width-large'}),
            'author': forms.TextInput(attrs={"class": 'uk-input uk-form-small uk-form-width-large', "value": "", "id":"authorID", "type":"hidden"}),
            #'author': forms.Select(attrs={"class": 'uk-select uk-form-small uk-form-width-large'}),
            'category': forms.Select(choices=category_list,attrs={"class": "uk-select uk-form-small uk-form-width-large"}),
            'slug': forms.TextInput(attrs={"class": 'uk-input uk-form-small uk-form-width-large'}),
            'body': forms.Textarea(attrs={"class": 'uk-textarea uk-form-small uk-form-width-large'}),
        }