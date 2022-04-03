from django.urls import path

from .models import SocialMedia
from .views import (
    ExperienceList,
    ExperienceDetail,
    CertificateList,
    CertificateDetail,
    SocialMediaList,
    SocialMediaDetail,
)

app_name = "blog"

urlpatterns = [
    path("experience/<int:pk>/", ExperienceDetail.as_view(), name="experience-detail"),
    path("experience/", ExperienceList.as_view(), name="experience-create"),
    # Certification urls
    path(
        "certificate/<int:pk>/", CertificateDetail.as_view(), name="certificate-detail"
    ),
    path("certificate/", CertificateList.as_view(), name="certificate-create"),
    # Social media account details
    path("social/<int:pk>/", SocialMediaDetail.as_view(), name="social-detail"),
    path("social/", SocialMediaList.as_view(), name="social-create"),
]
