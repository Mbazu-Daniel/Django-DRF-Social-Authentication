from datetime import datetime, timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from authentication.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
    return "project/{filename}".format(filename=filename)


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company = models.CharField(max_length=200, blank=False, null=False)
    position = models.CharField(max_length=200, blank=False, null=False)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.company


class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    host = models.CharField(max_length=200, blank=False, null=False)
    issue_date = models.DateField()

    def __str__(self):
        return self.host


class Contact(models.Model):
    last_name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=False)
    description = models.TextField()


class SocialMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    youtube_profile = models.URLField(blank=True, null=True)
    facebook_profile = models.URLField(blank=True, null=True)
    instagram_profile = models.URLField(blank=True, null=True)
    medium_profile = models.URLField(blank=True, null=True)
    github_profile = models.URLField(blank=True, null=True)
    hashnode_profile = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return str(self.user)


class Project(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="project_posts"
    )
    title = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(_("Image"), upload_to=upload_to, blank=True, null=True)
    description = models.TextField()
    project_link = models.URLField(null=True,  blank=True)
    result = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=200, blank=True, null=True)
    tools = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.title
    
    # class ProjectReview(models.Model):
    # project_review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # description = models.CharField(max_length=200, null=True)
    # project = models.ForeignKey(
    #     Project, on_delete=models.CASCADE, related_name="reviews"
    # )
    # active = models.BooleanField(default=True)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.project
