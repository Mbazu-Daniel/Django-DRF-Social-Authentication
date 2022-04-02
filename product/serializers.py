from rest_framework import serializers

from product.models import Certificate, Experience, SocialMedia


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia