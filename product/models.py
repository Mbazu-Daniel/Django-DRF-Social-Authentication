from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from authentication.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(upload_to="media")
    background = models.TextField()
    goal = models.TextField()
    result = models.TextField()
    duration = models.DateField()
    interpretation = models.TextField()
    tools = models.TextField()

    def __str__(self):
        return self.title


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
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField()
    description = models.TextField()


class SocialMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    linkedin_profile = models.URLField()
    youtube_profile = models.URLField()
    facebook_profile = models.URLField()
    instagram_profile = models.URLField()
    medium_profile = models.URLField()
    github_profile = models.URLField()
    hashnode_profile = models.URLField()
