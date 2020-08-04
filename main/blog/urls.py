from django.urls import path
from .views import AddPostView, HomeView, PostDetailView
#from .views import CourseView

urlpatterns = [
    path('', HomeView.as_view(), name="home"), # 3. Then imported here
    path('<slug:slug>/<int:pk>', PostDetailView.as_view(), name="post-detail"), # path for each post detail on click
    #path('<int:pk>', CourseView.as_view(), name="course-detail"), # path for each post detail on click
    path("add-post/", AddPostView.as_view(), name="add-post"),
]