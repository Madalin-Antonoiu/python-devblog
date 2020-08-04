from django.shortcuts import render
from .models import Post, Category, Course # this is our models.py file
from django.views.generic import ListView, DetailView, CreateView


class HomeView(ListView): #2. Then import this view into urls
    model = Post
    template_name = "home.html"

class PostDetailView(DetailView): #2. Then import this view into urls
    model = Post
    template_name = "post_detail.html"

class AddPostView(CreateView):
    model = Post
    template_name = 'Add_Post.html'
    fields = "__all__" # - Display all models.py/ Post entries
    #fields = ("title", "body") # - Display specific ones only


