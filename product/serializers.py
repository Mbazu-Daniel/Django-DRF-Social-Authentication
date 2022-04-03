from rest_framework import serializers
from .models import Project

from .models import Certificate, Experience, SocialMedia


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
    model = Project
    fields = "__all__"
