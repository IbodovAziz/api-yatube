from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    /api/v1/posts/ ; /api/v1/posts/{id}/
    """
    queryset = Post.objects.select_related('author').all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    /api/v1/groups/ ; /api/v1/groups/{id}/
    Только чтение.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    """
    /api/v1/posts/{post_id}/comments/
    /api/v1/posts/{post_id}/comments/{id}/
    """
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        # Возвращаем только комментарии конкретного поста
        return Comment.objects.select_related(
            'author', 'post'
        ).filter(post=self.get_post())

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, post=self.get_post()
        )
