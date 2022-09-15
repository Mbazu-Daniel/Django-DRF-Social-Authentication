from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    AbstractUser,
)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from phonenumber_field.modelfields import PhoneNumberField

from authentication.managers import UserManager
from authentication.validators import validate_file_size




AUTH_PROVIDERS = {
    "facebook": "facebook",
    "google": "google",
    "twitter": "twitter",
    "email": "email",
}


class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    avatar = models.ImageField(upload_to="store/images", validators=[validate_file_size], blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get("email")
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username", "phone_number"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}
