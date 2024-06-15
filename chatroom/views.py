from django.shortcuts import render

from rest_framework import permissions, authentication
from rest_framework.viewsets import ModelViewSet

from .models import UserProfile, Messages, Friend
from .serializers import UserProfileSerializer, MessagesSerializer, FriendSerializer

# Create your views here.


class UserProfileViewSet(ModelViewSet):
    """
    This view for UserProfile model with using ModelViewSet
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]


class MessagesViewSet(ModelViewSet):
    """
    This view for Messages model with using ModelViewSet
    """
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class FriendViewSet(ModelViewSet):
    """
    This view for Friend model with using ModelViewSet
    """
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
