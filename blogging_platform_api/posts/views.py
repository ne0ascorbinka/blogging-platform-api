from rest_framework import viewsets, filters
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    search_fields = ['title', 'content', 'category__name']

