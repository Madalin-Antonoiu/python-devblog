from django.shortcuts import render
from .models import Post, Category # this is our models.py file
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from django.urls import reverse_lazy

class HomeView(ListView): #2. Then import this view into urls
    model = Post
    template_name = "home.html"
    #ordering = ['-id'] - "-" means reverse order
    ordering = ['-updated_at']

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

class DeletePostView(DeleteView):
    model = Post
    template_name = "Delete_Post.html"
    success_url = reverse_lazy('home')