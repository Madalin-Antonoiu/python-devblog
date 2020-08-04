from django.urls import path
from .views import HomeView, PostDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"), # 3. Then imported here
    path('<int:pk>', PostDetailView.as_view(), name="post-detail") # path for each post detail on click
]