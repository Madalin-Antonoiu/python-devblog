from django.urls import path
from .views import HomeView, PostDetailView, CategoryView
#from .views import CourseView

urlpatterns = [
    path('', HomeView.as_view(), name="home"), # 3. Then imported here
    path('<str:category>', CategoryView.as_view(), name="category-detail"), # path for each post detail on click
]