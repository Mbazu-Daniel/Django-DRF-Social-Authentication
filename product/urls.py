from django.urls import include, path

from .models import SocialMedia
from .views import (
    ExperienceList,
    ExperienceDetail,
    CertificateList,
    CertificateDetail,
    SocialMediaList,
    SocialMediaDetail,
    ProjectList,
    ProjectDetail
)
from rest_framework.routers import DefaultRouter

app_name = "product"


urlpatterns = [
     # Certification urls
    path(
        "certificate/<int:pk>/", CertificateDetail.as_view(), name="certificate-detail"
    ),
    path("certificate/", CertificateList.as_view(), name="certificate-create"),
    
    #experience section 
    path("experience/<int:pk>/", ExperienceDetail.as_view(), name="experience-detail"),
    path("experience/", ExperienceList.as_view(), name="experience-create"),
    
      #Project section 
    path("project/<int:pk>/", ProjectDetail.as_view(), name="project-detail"),
    path("project/", ProjectList.as_view(), name="project-create"),
   
    # Social media account details
    path("social/<int:pk>/", SocialMediaDetail.as_view(), name="social-detail"),
    path("social/", SocialMediaList.as_view(), name="social-create"),
]
