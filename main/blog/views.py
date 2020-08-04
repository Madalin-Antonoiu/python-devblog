from django.shortcuts import render
from .models import Post # this is our models.py file
from django.views.generic import ListView, DetailView 


class HomeView(ListView): #2. Then import this view into urls
    model = Post
    template_name = "home.html"

class PostDetailView(DetailView): #2. Then import this view into urls
    model = Post
    template_name = "post_detail.html"