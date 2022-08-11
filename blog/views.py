from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Comment, Post
from .paginations import DefaultPagination
from .serializers import CommentSerializer, PostSerializer

# Create your views here.


class PostCreateListView(generics.ListCreateAPIView):
    queryset = Post.published.prefetch_related("comments").all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "post"]
    pagination_class = DefaultPagination


class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.published.prefetch_related("comments").all()


class CommentCreateListView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    