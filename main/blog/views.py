from django.shortcuts import render
from .models import Post, Category # this is our models.py file
from django.views.generic import ListView, DetailView 


class HomeView(ListView): #2. Then import this view into urls
    model = Post
    template_name = "home.html"

class PostDetailView(DetailView): #2. Then import this view into urls
    model = Post
    template_name = "post_detail.html"

class CourseView(ListView): #2. Then import this view into urls
    model = Category
    template_name = "course_detail.html"