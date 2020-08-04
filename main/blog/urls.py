from django.urls import path
from . import views #Import Views...

urlpatterns = [
    path('', views.home, name="home") # to use here as declared in views.py/ home
]