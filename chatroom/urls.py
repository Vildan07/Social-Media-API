from django.urls import path, include

from .views import UserProfileViewSet, MessagesViewSet, FriendViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserProfileViewSet)
router.register('message', MessagesViewSet)
router.register('friend', FriendViewSet)


urlpatterns = [
    path('', include(router.urls)),
]