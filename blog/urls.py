from django.urls import path
from .feeds import LatestPostFeed

from .views import (
    # AdminDeletePost,
    # AdminPostDetail,
    # AdminPostList,
    PostList,
    PostDetail,
    # AdminUpdatePost,
    AdminCreatePost,
    PostListDetailfilter,
    ReviewCreate,
    ReviewDetail,
    ReviewList,
    # UserReview,
    AdminPostUpdate,
    
)


app_name = "blog"

urlpatterns = [
    path("post/", PostList.as_view(), name="post-create"),
    path("post/<str:pk>/", PostDetail.as_view(), name="post-detail"),
    path("post/search/", PostListDetailfilter.as_view(), name="post-search"),
   
   
    # User Review
    path("review/<int:pk>/review-create/", ReviewCreate.as_view(), name="review-create"),
    path("review/<int:pk>/review/", ReviewDetail.as_view(), name="review-list"),
    path("review/", ReviewList.as_view(), name="user-review-detail"),

   
    # feeds
    path("blog/feed/", LatestPostFeed(), name="post_feed"),
  
     # Post Admin URLs
    path('portal/', AdminCreatePost.as_view(), name='portal-create'),
    path('portal/<int:pk>/', AdminPostUpdate.as_view(), name='portal-update'),
   
]
