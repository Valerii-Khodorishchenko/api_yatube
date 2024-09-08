from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet


router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')

comment_list = CommentViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)
comment_detail = CommentViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/', comment_list, name='comment-list'),
    path('posts/<int:post_id>/comments/<int:pk>/', comment_detail,
         name='comment-detail'),
]
