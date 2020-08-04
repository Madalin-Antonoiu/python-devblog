# This is how i add a class to every field from models.py and add it to DOM

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ( "title", "course", "author", "body", "slug")

        widgets = {
            'title': forms.TextInput(attrs={"class": 'uk-input uk-form-small uk-form-width-large'}),
            'course': forms.Select(attrs={"class": 'uk-select uk-form-small uk-form-width-large'}),
            'author': forms.Select(attrs={"class": 'uk-select uk-form-small uk-form-width-large'}),
            'slug': forms.TextInput(attrs={"class": 'uk-input uk-form-small uk-form-width-large'}),
            'body': forms.Textarea(attrs={"class": 'uk-textarea uk-form-small uk-form-width-large'}),
        }