from django.urls import path
from .views import HomeView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"), 
    path('<slug:slug>/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path("create-post/", CreatePostView.as_view(), name="create-post"),
    path("update-post/<slug:slug>/<int:pk>", UpdatePostView.as_view(), name="update-post"),
    path("delete/<slug:slug>/<int:pk>", DeletePostView.as_view(), name="delete-post"),
]