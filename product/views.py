from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from blog.models import Post
from blog.permissions import IsUserOrReadOnly
from blog.serializers import PostSerializer
from product.models import Experience, Certificate
from product.serializers import ExperienceSerializer, CertificateSerializer

"""
Creating and list out the blog created 
"""


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.postobjects.all()  # we are using the object we made in the model
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUserOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

"""
User job experience
"""
class ExperienceList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Experience.objects.all()  # we are using the object we made in the model
    serializer_class = ExperienceSerializer


class ExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUserOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = ExperienceSerializer

"""
User Certification and honors
"""

class CertificateList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Certificate.objects.all()  # we are using the object we made in the model
    serializer_class = ExperienceSerializer


class CertificateDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUserOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = CertificateSerializer
