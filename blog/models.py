from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

# from taggit.managers import TaggableManager
from authentication.models import User
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return "posts/{filename}".format(filename=filename)


class Post(models.Model):

    """
    This will filter the post that are marked as published only,
    therefore no need to filter this on the view section
    """

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    image = models.ImageField(_("Image"), upload_to=upload_to, blank=True, null=True)
    slug = models.SlugField(max_length=250, unique_for_date="published")
    published = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts"
    )
    status = models.CharField(max_length=10, choices=options, default="draft")
    objects = models.Manager()  # Default Manager
    postobjects = PostObjects()  # Custom manager

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.title


class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=200, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.review_user)
