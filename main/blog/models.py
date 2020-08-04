# Create your models here.
from django.db import models
from django.contrib.auth.models import User # Connect to the admin we declared earlier  
from django.urls import reverse
# Models = Template > Views > Urls > Admin - Make sure you declare them in all places

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default="Undefined", unique=True) # Whenever a new Course is created, you must pick a category it relates to :)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['title']

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(User, default="admin", on_delete = models.CASCADE) # foreign key comes from the User we created earlier
    course = models.ForeignKey(Course, null=True, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = models.TextField()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['title']

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        # return reverse("post-detail", args=(str(self.id)) ) # Returns to newly created post
        return reverse("home") # Returns home after POST
