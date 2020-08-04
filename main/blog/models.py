# Create your models here.
from django.db import models
from django.contrib.auth.models import User # Connect to the admin we declared earlier  


class Post(models.Model): #1. Then import it into views
    #course = models.ForeignKey(Course,  on_delete = models.CASCADE, default=Course.id)
    author = models.ForeignKey(User, default="admin", on_delete = models.CASCADE) # foreign key comes from the User we created earlier
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = models.TextField()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['title']

    def __str__(self):
        return self.title 

