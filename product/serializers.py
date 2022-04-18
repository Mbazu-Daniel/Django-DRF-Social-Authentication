from rest_framework import serializers
from .models import Certificate, Experience, SocialMedia, Project


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"
        
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # exclude = ['created']
        fields = "__all__"
