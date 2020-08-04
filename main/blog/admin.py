# Register your models here.
from django.contrib import admin
from .models import Post,Category

admin.site.register(Post) # Posts to be accessible from the admin area
admin.site.register(Category)