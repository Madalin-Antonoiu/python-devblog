from django.contrib import admin
from django.urls import path, include # Import include...

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")), # ...to include our app urls, in "app/urls.py" 
]