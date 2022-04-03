from django.conf import settings
from rest_framework import serializers
from blog.models import Post
from .models import PostReview


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "author", "excerpt", "content", "status"]


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PostReview
        exclude = ("project",)
