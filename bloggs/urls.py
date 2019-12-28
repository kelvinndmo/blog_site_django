from django.urls import path
from bloggs import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path("", PostListView.as_view(), name="home-blogs"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("post/<pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("about", views.about, name="about-blogs")
]
