from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from authentication.models import User


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
    linkedin_profile = models.CharField(max_length=200)
    youtube_profile = models.CharField(max_length=200)
    facebook_profile = models.CharField(max_length=200)
    instagram_profile = models.CharField(max_length=200)
    medium_profile = models.CharField(max_length=200)
    github_profile = models.CharField(max_length=200)
    hashnode_profile = models.CharField(max_length=200)
