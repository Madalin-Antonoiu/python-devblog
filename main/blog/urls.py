from django.urls import path
from .views import HomeView, CreatePostView, ReadPostView,  UpdatePostView, DeletePostView, CreateCategoryView, CategoryView,LikeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path("create-post/", CreatePostView.as_view(), name="create-post"), 
    path('<int:pk>', ReadPostView.as_view(), name="read-post"),
    path("update-post/<int:pk>", UpdatePostView.as_view(), name="update-post"),
    path("delete/<int:pk>", DeletePostView.as_view(), name="delete-post"),
    path("create-category/", CreateCategoryView.as_view(), name="create-category"), 
    path("category/<str:ctg>", CategoryView, name="category"), # CategoryView alone, functional statement in views.py
    path('like/<int:pk>', LikeView, name="like-post"),
]