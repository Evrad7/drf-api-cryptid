
from rest_framework.routers import SimpleRouter

from rest_framework_nested.routers import NestedDefaultRouter

from .comment.viewsets import CommentViewSet

from .post.viewsets import PostViewSet

from .auth.viewsets import LoginViewSet, RegisterViewSet, RefreshViewSet


from .user.views import UserViewSet

router=SimpleRouter()

router.register(r"user", UserViewSet, basename="user")
router.register(r"auth/register", RegisterViewSet, basename="auth_register")
router.register(r"auth/login", LoginViewSet, basename="auth_login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth_refresh")
router.register(r"post", PostViewSet, basename="post")

post_router=NestedDefaultRouter(router, r"post", lookup="post")
post_router.register(r"comment", CommentViewSet, basename="post_comment")


urlpatterns=[
    *router.urls,
    *post_router.urls,
]