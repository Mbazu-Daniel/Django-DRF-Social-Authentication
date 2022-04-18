from django.shortcuts import get_object_or_404
from rest_framework import generics, filters, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Post, Review
from .permissions import IsAdminOrReadOnly, IsUserOrReadOnly
from .serializers import PostSerializer, ReviewSerializer

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

"""
Creating blog view with permissions set to only admin 

Creating and list out the blog created 
"""


class PostList(generics.ListAPIView):
    # permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.postobjects.all()


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        return get_object_or_404(Post, slug=item)


# Post Search


class PostListDetailfilter(generics.ListAPIView):

    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    # search_fields = ['^slug']
    # '^' Starts-with search.
    # '=' Exact matches.
    # "@" full database search
    search_fields = ["@slug"]


# Post Admin Section
# class AdminPostList(generics.ListAPIView):
#     permission_classes = [IsAdminOrReadOnly]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer

class AdminCreatePost(generics.ListCreateAPIView):
    # permission_classes = [IsAdminOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = PostSerializer
    queryset = Post.postobjects.all()
    


class AdminPostUpdate(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.postobjects.all()
    
    
    


    # def post(self, request, format=None):
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        username = self.request.query_params.get('username', None)
        return Review.objects.filter(review_user__username=username)


class ReviewList(generics.ListAPIView):

    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend]


    # def get_queryset(self):
    #     username = self.request.query_params.get("username", None)
    #     return Review.objects.filter(review_user__username=username)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsReviewUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    


class ReviewCreate(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
