from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import PermissionDenied

from posts.models import Comment, Group, Post
from .serializers import CommentSerializer, PostSerializer, GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_object(self):
        post = super().get_object()
        if (
            self.request.method in ['PUT', 'PATCH', 'DELETE']
            and post.author != self.request.user
        ):
            raise PermissionDenied(
                'Изменение или удаление чужого контента запрещено!'
            )
        return post


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(
            post_id=self.kwargs['post_id']
        ).select_related('post')

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    def get_object(self):
        comment = super().get_object()
        if (
            self.request.method in ['PUT', 'PATCH', 'DELETE']
            and comment.author != self.request.user
        ):
            raise PermissionDenied(
                'Изменение или удаление чужого контента запрещено!'
            )
        return comment
