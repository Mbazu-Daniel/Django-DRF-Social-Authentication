from django.urls import path

# from .views import PostList, PostDetail
from rest_framework.routers import DefaultRouter
from .views import BlogPost

app_name = "blog"

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
#     path('', PostList.as_view(), name='post-create'),
# ]

router = DefaultRouter()
router.register("", BlogPost, basename="post")
urlpatterns = router.urls
