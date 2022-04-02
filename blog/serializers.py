from django.conf import settings
from rest_framework import serializers
from blog.models import Post
from product.models import Review


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "author", "excerpt", "content", "status"]


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ("project",)
