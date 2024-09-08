from django.shortcuts import render
from rest_framework import viewsets

from .serializers import Post, PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
