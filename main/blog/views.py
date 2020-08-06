from django.shortcuts import render
from .models import Post, Category # this is from our models.py file
from django.views.generic import ListView, CreateView, DetailView,  UpdateView, DeleteView
from .forms import PostForm
from django.urls import reverse_lazy

class HomeView(ListView): #2. Then import this view into urls
    model = Post
    template_name = "home.html"
    #ordering = ['-id'] - "-" means reverse order
    ordering = ['-updated_at']

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'CRUD/Create_Post.html'
    # fields = "__all__" # - Display all models.py/ Post entries ( No longer needed with form_class)
    #fields = ("title", "body") # - Display specific ones only

class ReadPostView(DetailView): #2. Then import this view into urls
    model = Post
    template_name = "CRUD/Read_Post.html"

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm #You can always mirror PostForm and create an Edit Form class with certain fields only
    template_name = "CRUD/Update_Post.html"
    #fields = ['title', 'slug', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = "CRUD/Delete_Post.html"
    success_url = reverse_lazy('home')

class CreateCategoryView(CreateView):   
    model = Category
    fields = "__all__"
    template_name = 'Category/Create_Category.html'

# Showcasing functional way, as oposed to class way, request refers to the part of the url "category/"
def CategoryView(request, ctg):
    category_posts = Post.objects.filter(category=ctg.replace('-', ' ')) # filter(field = what we pass in)
    return render(request, "Category/Category.html", {'ctg': ctg.replace('-', ' '), 'category_posts': category_posts}) # i return : category/ sports or w/e
    #.title().replace('-', ' ')