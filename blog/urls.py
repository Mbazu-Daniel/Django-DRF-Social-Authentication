from django.urls import path

from .views import PostList, PostDetail
from rest_framework.routers import DefaultRouter

# from .views import BlogPost

app_name = "post"

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="blog-detail"),
    path("", PostList.as_view(), name="blog-create"),
]

# router = DefaultRouter()
# router.register("", BlogPost, basename="post")
# urlpatterns = router.urls
