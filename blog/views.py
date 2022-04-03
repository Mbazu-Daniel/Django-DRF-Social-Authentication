from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from blog.models import Post, PostReview
from .permissions import IsAdminOrReadOnly, IsUserOrReadOnly
from .serializers import PostSerializer, ReviewSerializer
from rest_framework.permissions import (
    IsAuthenticated,
)

# Create your views here.

"""
Creating blog view with permissions set to only admin 

Creating and list out the blog created 
"""


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.postobjects.all()  # we are using the object we made in the model
    serializer_class = PostSerializer

    # overwrite get objects
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        return get_object_or_404(Post, slug=item)


class PostDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


"""
Review session
"""


# Create your views here.
class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer

    #
    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return Review.objects.filter(review_user__username = username)

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        return PostReview.objects.filter(review_user__username=username)


class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    filterset_fields = ["review_user__username", "active"]

    # override queryset
    def get_queryset(self):
        pk = self.kwargs["pk"]
        return PostReview.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostReview.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsUserOrReadOnly]
    throttle_scope = "review-detail"


class ReviewCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    # throttle_classes = [ReviewCreateThrottle]

    def get_queryset(self):
        return PostReview.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        post = Post.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = PostReview.objects.filter(post=post, review_user=review_user)
