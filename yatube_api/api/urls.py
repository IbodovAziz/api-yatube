from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')


comments = [
    path('posts/<int:post_id>/comments/',
         CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='comment-list'),
    path('posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view(
             {
                 'get': 'retrieve', 'put': 'update',
                 'patch': 'partial_update', 'delete': 'destroy'
             }
         ),
         name='comment-detail'),
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(comments)),
]
