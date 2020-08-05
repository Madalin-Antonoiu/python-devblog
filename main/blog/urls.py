from django.urls import path
from .views import AddPostView, HomeView, PostDetailView, UpdatePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"), 
    path('<slug:slug>/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path("add-post/", AddPostView.as_view(), name="add-post"),
    path("update-post/<slug:slug>/<int:pk>", UpdatePostView.as_view(), name="update-post"),
]