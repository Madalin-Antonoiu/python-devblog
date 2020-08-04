from django.shortcuts import render
from .models import Post, Category, Course # this is our models.py file
from django.views.generic import ListView, DetailView, CreateView

class AddPostView(CreateView):
    model = Post
    template_name = 'Add_Post.html'
    fields = "__all__"

class HomeView(ListView): #2. Then import this view into urls
    model = Post
    template_name = "home.html"

class PostDetailView(DetailView): #2. Then import this view into urls
    model = Post
    template_name = "post_detail.html"

class CategoryView(ListView): #2. Then import this view into urls
    model = Category
    template_name = "category_detail.html"

class CourseView(DetailView): #2. Then import this view into urls
    model = Course
    template_name = "course_detail.html"

