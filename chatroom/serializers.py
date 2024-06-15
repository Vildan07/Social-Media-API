from rest_framework import serializers
from .models import UserProfile, Messages, Friend


class UserProfileSerializer(serializers.ModelSerializer):
    """
    This serializer is used to serialize UserProfile objects
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ('id',)


class MessagesSerializer(serializers.ModelSerializer):
    """
    This serializer is used to serialize Messages objects
    """
    class Meta:
        model = Messages
        fields = '__all__'
        read_only_fields = ('id',)


class FriendSerializer(serializers.ModelSerializer):
    """
    This serializer is used to serialize Friend objects
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Friend
        fields = '__all__'
        read_only_fields = ('id',)
