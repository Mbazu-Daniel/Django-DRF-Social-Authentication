from rest_framework import generics, viewsets
from rest_framework.decorators import permission_classes

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from blog.models import Post
from .permissions import IsAdminOrReadOnly
from .serializers import PostSerializer
from rest_framework.permissions import (
    BasePermission,
    DjangoModelPermissionsOrAnonReadOnly,
    SAFE_METHODS,
    DjangoModelPermissions,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)


# Create your views here.

"""
Creating view using modelviewset
"""


class BlogPost(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer

    # overwrite get objects
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)


    # custom queryset
    def get_queryset(self):
        return Post.objects.all()