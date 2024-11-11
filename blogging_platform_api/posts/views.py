from rest_framework import viewsets, filters
from .models import Post
from .serializers import PostSerializer


class TermSearchFilter(filters.SearchFilter):
    search_param = 'term'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [TermSearchFilter]
    search_fields = ['title', 'content', 'category__name']

