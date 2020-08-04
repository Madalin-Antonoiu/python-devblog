from django.urls import path
from .views import HomeView, PostDetailView
#from .views import CourseView

urlpatterns = [
    path('', HomeView.as_view(), name="home"), # 3. Then imported here
    path('<slug:slug>', PostDetailView.as_view(), name="post-detail"), # path for each post detail on click
    # path('course/', CourseView.as_view(), name="course-detail")
]