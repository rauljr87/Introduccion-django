from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView

app_name = "blog"

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('create/', BlogCreateView.as_view(), name="create"),
    # llama a los post por su pk
    path('<int:pk>/', BlogDetailView.as_view(), name="detail")
]
