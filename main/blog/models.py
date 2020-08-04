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


class Post(models.Model): #1. Then import it into views
    prepopulated_fields = {"slug": ("title")}

    author = models.ForeignKey(User, default="admin", on_delete = models.CASCADE) # foreign key comes from the User we created earlier
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, default=Category, on_delete = models.CASCADE) # it widraws the database entries from class Category!
    subcategory = models.CharField(max_length=255, default="")
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)




    # def get_absolute_url(self):
    #     kwargs = {
    #         'pk': self.id,
    #         'slug': self.slug
    #     }
    #     return reverse('subcategory-pk-slug-title', kwargs=kwargs)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)