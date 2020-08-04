# Create your models here.
from django.db import models
from django.contrib.auth.models import User # Connect to the admin we declared earlier  


class Category(models.Model): #1. Then import it into views
    title = models.CharField(max_length=255, unique=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

class Course(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,  on_delete = models.CASCADE) # Whenever a new Course is created, you must pick a category it relates to :)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['category']

    def __str__(self):
        return self.name


class Post(models.Model): #1. Then import it into views
    category = models.ForeignKey(Category, default=Category, on_delete = models.CASCADE) # it widraws the database entries from class Category!
    course = models.ForeignKey(Course,  on_delete = models.CASCADE, default=Course.id)
    author = models.ForeignKey(User, default="admin", on_delete = models.CASCADE) # foreign key comes from the User we created earlier
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

