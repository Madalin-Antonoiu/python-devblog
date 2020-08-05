# Register your models here.
from django.contrib import admin
from .models import Post, Category

class Prepopulate(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, Prepopulate) # Posts to be accessible from the admin area
admin.site.register(Category)
