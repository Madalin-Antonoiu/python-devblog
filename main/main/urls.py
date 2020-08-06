from django.contrib import admin
from django.urls import path, include # Import include...

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")), # ...to include our app urls, in "app/urls.py" 

    # We need to declare them both, AND in this order. The second line is if we declare 
    # other auth related pages except the basic ones that are provided by django.contrib.auth, 
    # it needs to know where to go.
    path('authentication/', include("django.contrib.auth.urls")), # will take care off all the urls for us
    path('authentication/', include("authentication.urls")),
]