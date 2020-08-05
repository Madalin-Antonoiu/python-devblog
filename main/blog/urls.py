from django.urls import path
from .views import HomeView, CreatePostView, ReadPostView,  UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path("create-post/", CreatePostView.as_view(), name="create-post"), 
    path('<slug:slug>/<int:pk>', ReadPostView.as_view(), name="read-post"),
    path("update-post/<slug:slug>/<int:pk>", UpdatePostView.as_view(), name="update-post"),
    path("delete/<slug:slug>/<int:pk>", DeletePostView.as_view(), name="delete-post"),
]