from django.shortcuts import get_object_or_404, render
from rest_framework import generics
# from blog.permissions import IsUserOrReadOnly
from .models import Experience, Certificate, SocialMedia,Project
from .serializers import (
    ExperienceSerializer,
    CertificateSerializer,
    SocialMediaSerializer,
    ProjectSerializer
)
from rest_framework.parsers import FormParser, MultiPartParser

"""
User job experience
"""


class ExperienceList(generics.ListCreateAPIView):
    # permission_classes = [IsUserOrReadOnly]
    queryset = Experience.objects.all()  # we are using the object we made in the model
    serializer_class = ExperienceSerializer


class ExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsUserOrReadOnly]
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


"""
User Certification and honors
"""


class CertificateList(generics.ListCreateAPIView):
    # permission_classes = [IsUserOrReadOnly]
    queryset = Certificate.objects.all()  # we are using the object we made in the model
    serializer_class = CertificateSerializer


class CertificateDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsUserOrReadOnly]
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


"""
User Social media accounts details
"""


class SocialMediaList(generics.ListCreateAPIView):
    # permission_classes = [IsUserOrReadOnly]
    queryset = SocialMedia.objects.all()  # we are using the object we made in the model
    serializer_class = SocialMediaSerializer


class SocialMediaDetail(generics.RetrieveUpdateAPIView):
    # permission_classes = [IsUserOrReadOnly]
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer




class ProjectList(generics.ListCreateAPIView):
    # permission_classes = [IsUserOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    queryset = Project.objects.all()  # we are using the object we made in the model
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsUserOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
