from django.shortcuts import render
from .models import Post, Category, Course # this is our models.py file
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostForm

class HomeView(ListView): #2. Then import this view into urls
    model = Post
    template_name = "home.html"

class PostDetailView(DetailView): #2. Then import this view into urls
    model = Post
    template_name = "post_detail.html"

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Add_Post.html'
    # fields = "__all__" # - Display all models.py/ Post entries ( No longer needed with form_class)
    #fields = ("title", "body") # - Display specific ones only


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm #You can always mirror PostForm and create an Edit Form class with certain fields only
    template_name = "Update_Post.html"
    #fields = ['title', 'course', 'slug', 'body']
